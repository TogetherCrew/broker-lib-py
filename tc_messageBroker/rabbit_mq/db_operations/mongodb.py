import logging
from typing import Any, Optional

import jsonschema
from jsonschema.exceptions import ValidationError
from pymongo import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern

from tc_messageBroker.rabbit_mq.saga.utils.choreography_schema import (  # isort: skip
    choreography_schema,
)


class MongoDB:
    def __init__(self, connection_str: str, db_name: str, collection_name: str) -> None:
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
        self.client: Optional[MongoClient] = None

    def connect(self) -> None:
        """
        connect to MongoDB database
        """
        client: MongoClient = MongoClient(host=self.connection_str)
        self.client = client

    def replace(self, sagaId: str, data: dict):
        """
        replace a document with the new data

        Parameters:
        -------------
        sagaId : str
            used to find the document we're going to replace
        data : dict
            the data we're going to replace the document with
        """
        valid = self._validator([data])

        def callback_wrapper(session):
            self._write_db(
                session, data, mode="replace", replace_query={"sagaId": sagaId}
            )

        if valid:
            if self.client is not None:
                with self.client.start_session() as session:
                    session.with_transaction(
                        callback=callback_wrapper,
                        read_concern=ReadConcern("local"),
                        write_concern=WriteConcern("local"),
                    )
            else:
                raise ConnectionError("No connection to MongoDB from broker library!")

    def write(self, data: list[dict]):
        """
        write the data into db
        """
        valid = self._validator(data)

        if valid:
            if self.client is not None:
                with self.client.start_session() as session:
                    session.with_transaction(
                        callback=lambda session: self._write_db(session, data),
                        read_concern=ReadConcern("local"),
                        write_concern=WriteConcern("local"),
                    )
            else:
                raise ConnectionError("No connection to MongoDB from broker library!")

    def read(self, query: dict = {}, count: int = 1) -> Optional[list] | dict[str, Any]:
        """
        read from database (using find method)

        Parameters:
        -------------
        query : dict
            the query to find a specific data
            default is `{}` which would mean to return all data
        count : int
            the count of samples to get
            if 1 then findOne method is used
            else the find method in mongoClient is used

        Returns:
        ---------
        data : Optional[list] | dict[str, Any]
            a list of data or one dictionary would be returned
            based on the count of data requested
            if count equal to 1 then one python dictionary would be returned
            else a list is going to be returned
        """
        if self.client is None:
            raise ConnectionError("Not connected to mongodb instance!")

        if count == 1:
            cursor = self.client[self.db_name][self.collection_name].find_one(query)
            data = cursor
        else:
            cursor = (
                self.client[self.db_name][self.collection_name].find(query).limit(count)
            )
            data = list(cursor)

        return data

    def delete(self, query: dict):
        """
        delete documents

        Parameters:
        -------------
        query : dict
            the query to delete documents we want
        """
        if self.client is None:
            raise ConnectionError("Not connected to mongodb instance!")

        with self.client.start_session() as session:
            session.with_transaction(
                callback=lambda session: self._write_db(
                    session, data=None, mode="delete", delete_query=query
                ),
                read_concern=ReadConcern("local"),
                write_concern=WriteConcern("local"),
            )

    def _write_db(
        self, session, data: Optional[list[dict]], mode="add", **kwargs
    ) -> None:
        """
        writing the data into db within a session
        (creating the transaction)

        Parameters:
        -------------
        session : MongoClient.session
            the session we want to use for writing operations on db
        data : Optional[list[dict]]
            the data we're going to write
        mode: str
            we're going to either `add`, `replace` or `delete`
        **kwargs:
            replace_query : dict
                if our mode is replace, then we should use a dictionary to query
                the document we want to replace
            delete_query : dict
                if our mode is delete, then we should use a dictionary to query
                the documents we want to delete
        """

        try:
            match mode:
                case "add":
                    session.client[self.db_name][self.collection_name].insert_many(data)
                case "replace":
                    session.client[self.db_name][self.collection_name].replace_one(
                        kwargs["replace_query"], data
                    )
                case "delete":
                    session.client[self.db_name][self.collection_name].delete_many(
                        kwargs["delete_query"]
                    )
                case _:
                    logging.error(f"The writing mode: {mode} is not implemented!")
        except KeyError as exp:
            logging.error(f"{exp}: unsufficient function inputs!")
        except Exception as exp:
            logging.error(f"Error occured: {exp}")

    def _validator(self, data: list[dict]):
        """
        validate the schema of data before saving it to db

        Parameters:
        ------------
        data : dict
            a nested python dict
        """
        try:
            for document in data:
                jsonschema.validate(
                    instance=document,
                    schema=choreography_schema,
                )
            return True
        except ValidationError as error:
            logging.error(f"Not valid schema to save in DB! Error: {error}")
            return False
