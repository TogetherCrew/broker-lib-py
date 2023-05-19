from pymongo import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
from tc_messageBroker.rabbit_mq.saga.utils.choreography_schema import (
    choreography_schema,
)
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import logging


class MongoDB:
    def __init__(
        self, connection_str: str, db_name: str = "RnDAO", collection_name: str = "Saga"
    ) -> None:
        """
        initialize the mongodb class

        Parameters:
        -------------
        connection_str : str
            the url to connect to mongo_db
        db_name : str
            the database we need
        collection_name : str
            name of the collection that we would use
        """
        self.connection_str = connection_str
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None

    def connect(self) -> None:
        """
        connect to MongoDB database
        """
        client = MongoClient(host=self.connection_str)
        self.client = client

    def write(self, data):
        """
        write the data into db
        """
        valid = self._validator(data)

        if valid:
            with self.client.start_session() as session:
                session.with_transaction(
                    callback=lambda session: self._write_db(session, data),
                    read_concern=ReadConcern("local"),
                    write_concern=WriteConcern("local"),
                )

    def read(self, query={}) -> list:
        """
        read from database (using find method)

        Parameters:
        -------------
        query : dict
            the query to find a specific data
            default is `{}` which would return all data
        """

        cursor = self.client[self.db_name][self.collection_name].find({})

        return list(cursor)

    def _write_db(self, session, data):
        """
        writing the data into db within a session
        (creating the transaction)
        """
        session.client[self.db_name][self.collection_name].insert_many(data)

    def _validator(self, data):
        """
        validate the schema of data before saving it to db

        Parameters:
        ------------
        data : dict
            a nested python dict
        """
        try:
            validate(instance=data, schema=choreography_schema)
            return True
        except ValidationError as error:
            logging.error(f"Not valid schema to save in DB! Error: {error}")
            return False
