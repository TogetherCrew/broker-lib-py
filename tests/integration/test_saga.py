"""
testing the saga object
"""
import os
from copy import deepcopy
from datetime import datetime

import numpy as np
from dotenv import load_dotenv
from tc_messageBroker.rabbit_mq.db_operations import MongoDB
from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.saga_base import Saga, get_saga
from tc_messageBroker.rabbit_mq.saga.transactions import (
    DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)
from tc_messageBroker.rabbit_mq.status import Status


def test_inputs():
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    saga_db = os.getenv("DB_SAGA_NAME")
    saga_collection = os.getenv("DB_SAGA_COLLECTION_NAME")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    mongodb = MongoDB(
        connection_str=connection_url, db_name=saga_db, collection_name=saga_collection
    )
    mongodb.connect()
    mongodb.client[saga_db].drop_collection(saga_collection)
    mongodb.client[saga_db].create_collection(saga_collection)

    # we should have this data before running this test in db
    saga = get_saga(
        sagaId="something",
        connection_url=connection_url,
        db_name=saga_db,
        collection=saga_collection,
    )
    assert saga is None


def test_saga_update():
    """
    test updating a saga instance in db
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_creds = {}
    connection_creds["connection_str"] = f"mongodb://{user}:{password}@{host}:{port}"
    connection_creds["db_name"] = os.getenv("DB_SAGA_NAME")
    connection_creds["collection_name"] = os.getenv("DB_SAGA_COLLECTION_NAME")

    choreography = IChoreography(
        name="sample", transactions=deepcopy(DISCORD_UPDATE_CHANNELS_TRANSACTIONS)
    )

    saga = Saga(
        choreography=choreography,
        status=Status.NOT_STARTED,
        data={"guildId": "1234"},
        created_at=datetime.now(),
    )

    tx = np.array(choreography.transactions)
    tx[0].status = Status.SUCCESS

    saga._update_save(transactions=tx, mongo_creds=connection_creds)
