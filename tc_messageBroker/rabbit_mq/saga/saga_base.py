from .choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.status import Status
from tc_messageBroker import RabbitMQ
import uuid
from datetime import datetime
import numpy as np
from tc_messageBroker.rabbit_mq.db_operations import MongoDB


class Saga:
    def __init__(
        self,
        choreography: IChoreography,
        status: str,
        data: any,
        created_at: datetime,
        sagaId: str = None,
    ) -> None:
        self.uuid = sagaId if sagaId is not None else str(uuid.uuid1())
        self.choreography = choreography
        self.status = status
        self.data = data
        self.created_at = created_at

    def next(
        self,
        publish_method: RabbitMQ.publish | RabbitMQ.publish_on_exchange,
        call_function: callable,
        mongo_connection: str,
    ):
        """
        calling the next transaction within the saga
        and updating the saga state in db

        Parameters:
        ------------
        publish_method : RabbitMQ.publish
            the publish methods that are from the RabbitMQ
        call_function : callable
            a function to be called when the message recieved
        mongo_connection : str
            the mongodb connection url to update the db
        """
        transactions = self.choreography.transactions

        ## get the transactions with status NOT_STARTED
        tx_not_started = []
        ## other transactions
        tx_other = []

        for tx in transactions:
            if tx.status == Status.NOT_STARTED:
                tx_not_started.append(tx)
            else:
                tx_other.append(tx)

        ## converting to numpy in order to
        ## make the slices of array pointing to one place in memory
        tx_not_started = np.array(tx_not_started)
        tx_other = np.array(tx_other)

        tx_orders = [tx.order for tx in tx_not_started]

        sorted_indices = np.argsort(tx_orders)

        current_tx = tx_not_started[sorted_indices[0]]

        current_tx.status = Status.IN_PROGRESS
        current_tx.start = datetime.now()

        self._update_save(
            tx_tuple=(tx_not_started, tx_other), mongo_connection=mongo_connection
        )

        try:
            ## the function we would call
            result = call_function()

            current_tx.status = Status.SUCCESS
            current_tx.end = datetime.now()
            current_tx.runtime = (current_tx.end - current_tx.start).timestamp() * 1000

            ## if we ran the last transaction
            if len(tx_not_started) == 1:
                self.status = Status.SUCCESS
            else:
                next_tx = tx_not_started[sorted_indices[1]]
                publish_method(
                    queue_name=next_tx.queue,
                    event=next_tx.event,
                    content={"uuid": self.uuid, "data": result},
                )

            self._update_save(
                tx_tuple=(tx_not_started, tx_other), mongo_connection=mongo_connection
            )

        except Exception as exp:
            current_tx.error = str(exp)
            current_tx.status = Status.FAILED

            self._update_save(
                tx_tuple=(tx_not_started, tx_other), mongo_connection=mongo_connection
            )

    def _update_save(self, tx_tuple: tuple(list, list), mongo_connection):
        """
        update the transactions in saga choreography and then save data to db
        """
        ## save the status into DB
        mongodb = MongoDB(mongo_connection)
        data = self._create_data()

        transactions = [tx_tuple[0]]
        transactions.extend(tx_tuple[1])

        ## creating a duplicate choreography to avoid shallow copy
        choreography = IChoreography(
            name=self.choreography.name, transactions=transactions
        )

        self.choreography = choreography

        ## update the available choreography
        mongodb.replace(sagaId=self.uuid, data=data)

    def _create_data(self) -> dict[str, any]:
        """
        create the data from the properties of the class
          as we had in db schema

        Returns:
        ---------
        data : dict[str, any]
            the dictionary representing the current saga document

        """
        data = {}

        data["choreography"] = self.choreography
        data["status"] = self.status
        data["data"] = self.data
        data["sagaId"] = self.uuid
        data["createdAt"] = self.created_at
        data["updatedAt"] = datetime.now()

        return data
