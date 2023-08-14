import os

from dotenv import load_dotenv
from tc_messageBroker.rabbit_mq.db_operations.mongodb import MongoDB


def test_mongo_class():
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )

    assert mongodb.connection_str == connection_url
    assert mongodb.db_name == db_name
    assert mongodb.collection_name == collection_name
    assert mongodb.client is None


def test_credentials():
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")

    assert host is not None
    assert user is not None
    assert port is not None
    assert password is not None
    assert db_name is not None
    assert collection_name is not None
