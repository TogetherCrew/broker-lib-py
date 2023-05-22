from .choreography_base import IChoreography
from .transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.status import Status
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
        publish_method: callable,
        call_function: callable,
        mongo_connection: str,
        test_mode=False,
    ):
        """
        calling the next transaction within the saga
        and updating the saga state in db

        Parameters:
        ------------
        publish_method : RabbitMQ.publish | RabbitMQ.publish_on_exchange
            the publish methods that are from the RabbitMQ
        call_function : callable
            a function to be called when the message recieved
        mongo_connection : str
            the mongodb connection url to update the db
        test_mode : bool
            testing the function indicates that we wouldn't read or write on DB
            default is False
        """
        tx_sorted, tx_not_started_count = self._sort_transactions(
            self.choreography.transactions
        )

        self.status = Status.IN_PROGRESS

        ## get the first order transaction
        current_tx = tx_sorted[0]

        current_tx.status = Status.IN_PROGRESS
        current_tx.start = datetime.now()

        self._update_save(
            transactions=tx_sorted, mongo_connection=mongo_connection, test=test_mode
        )

        try:
            ## the function we would call
            result = call_function()

            current_tx.status = Status.SUCCESS
            current_tx.end = datetime.now()
            ## in miliseconds format
            current_tx.runtime = (current_tx.end - current_tx.start).microseconds / 1000

            ## if we ran the last transaction
            if tx_not_started_count == 1:
                self.status = Status.SUCCESS
            else:
                next_tx = tx_sorted[1]
                publish_method(
                    queue_name=next_tx.queue,
                    event=next_tx.event,
                    content={"uuid": self.uuid, "data": result},
                )

            self._update_save(
                transactions=tx_sorted,
                mongo_connection=mongo_connection,
                test=test_mode,
            )

        except Exception as exp:
            current_tx.error = str(exp)

            if current_tx.status != Status.SUCCESS:
                current_tx.status = Status.FAILED

            self.status = Status.FAILED

            self._update_save(
                transactions=tx_sorted,
                mongo_connection=mongo_connection,
                test=test_mode,
            )

    def _sort_transactions(self, transactions: list[ITransaction]):
        """
        sort transactions by their order and status
        the NOT_STARTED ones would be at the first of the list
        and they are ordered by `order` property

        Parameters:
        ------------
        transactions : list[ITransaction]
            the list of transactions to order

        Returns:
        ---------
        transactions_ordered : ndarray(ITransaction)
            the transactions ordered by status
            the `NOT_STARTED` ones are the firsts
            it is actually a numpy array for us to be able to
              change the properties in deep memory
        tx_not_started_count : int
            the not started transactions count
        """
        tx_not_started = []
        tx_other = []

        for tx in transactions:
            if tx.status == Status.NOT_STARTED:
                tx_not_started.append(tx)
            else:
                tx_other.append(tx)

        tx_not_started_count = len(tx_not_started)
        tx_not_started_sorted = self._sort_transactions_orderly(tx_not_started)

        transactions_ordered = list(tx_not_started_sorted)
        transactions_ordered.extend(tx_other)

        return np.array(transactions_ordered), tx_not_started_count

    def _sort_transactions_orderly(self, transactions: list[ITransaction]):
        """
        sort transactions by their `order` property

        Parameters:
        ------------
        transactions : list[ITransaction]
            the list of transactions to order

        Returns:
        ---------
        transactions_orderly_sorted : list[ITransaction]
            transactions sorted by their order
        """
        orders = [tx.order for tx in transactions]
        sorted_indices = np.argsort(orders)

        return np.array(transactions)[sorted_indices]

    def _update_save(
        self, transactions: list[ITransaction], mongo_connection, test=False
    ):
        """
        update the transactions in saga choreography and then save data to db

        test is the test mode which it does not interact with db.
        default is False meaning we have to have an interaction with db
        """
        if not test:
            ## save the status into DB
            mongodb = MongoDB(mongo_connection)
            mongodb.connect()
            data = self._create_data()

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


def get_saga(guildId, connection_url):
    """
    get saga object for a special guild

    Parameters:
    ------------
    guildId : str
        the guildId which the saga belongs to
    connection_url : str
        the connection to db which the saga architecture is saved

    Returns:
    ----------
    saga_obj : Saga
        the saga object to use
    """
    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    data = mongodb.read(query={"data.guildId": guildId}, count=1)

    saga_obj = Saga(
        choreography=data["choreography"],
        status=data["status"],
        created_at=data["createdAt"],
        sagaId=data["sagaId"],
        data=data["data"],
    )

    return saga_obj
