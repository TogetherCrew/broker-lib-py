import os
from copy import deepcopy
from datetime import datetime, timedelta

from dotenv import load_dotenv
from numpy.random import randint
from tc_messageBroker.rabbit_mq.db_operations import MongoDB


def test_insert_one():
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"

    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()

    data = create_random_data()

    mongodb.write(data=[data])


def test_insert_multiple():
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()

    documents = []
    for _ in range(5):
        data = create_random_data()
        documents.append(data)

    mongodb.write(data=documents)


def test_read_count_one():
    """
    read from db after writing using the previous function (above)
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()

    mongodb.client[db_name].drop_collection(collection_name)
    mongodb.client[db_name].create_collection(collection_name)
    data = create_random_data()

    mongodb.write(data=[data])
    print(f"data is: {data}")

    results = mongodb.read(query={}, count=1)
    print(f"results: {results}")

    assert isinstance(results, dict) is True
    assert "choreography" in results.keys()
    assert "status" in results.keys()
    assert "data" in results.keys()
    assert "sagaId" in results.keys()
    assert "createdAt" in results.keys()
    assert "updatedAt" in results.keys()


def test_read_count_multiple():
    """
    read from db after writing using the previous function (above)
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()
    mongodb.client[db_name].drop_collection(collection_name)
    mongodb.client[db_name].create_collection(collection_name)

    documents = []
    data_count = 5
    for _ in range(data_count):
        data = create_random_data()
        documents.append(data)

    mongodb.write(data=documents)

    results = mongodb.read(query={}, count=data_count)

    assert isinstance(results, list) is True
    assert len(results) == data_count

    for i in range(data_count):
        assert "choreography" in results[i].keys()
        assert "status" in results[i].keys()
        assert "data" in results[i].keys()
        assert "sagaId" in results[i].keys()
        assert "createdAt" in results[i].keys()
        assert "updatedAt" in results[i].keys()


def test_replace():
    """
    test replacing a document we just inserted
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()
    mongodb.client[db_name].drop_collection(collection_name)
    mongodb.client[db_name].create_collection(collection_name)

    data = create_random_data()

    mongodb.write(data=[data])
    data.pop("_id")

    new_data = deepcopy(data)

    choreography_name = "NEW_TEST"
    tx_state = "SUCCESS"

    new_data["choreography"]["name"] = choreography_name
    new_data["choreography"]["name"] = choreography_name
    new_data["choreography"]["transactions"][0]["status"] = tx_state

    mongodb.replace(data["sagaId"], new_data)

    document = mongodb.read({"sagaId": new_data["sagaId"]})
    document.pop("_id")

    assert document != data
    assert document == new_data


def test_delete():
    """
    delete all except one of the ligitimate data which we choose
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )
    mongodb.connect()
    mongodb.client[db_name].drop_collection(collection_name)
    mongodb.client[db_name].create_collection(collection_name)

    mongodb.delete(query={"data.guildId": {"$ne": "993163081939165234"}})


def test_wrong_input():
    """
    give wrong input to insert
    """
    load_dotenv()
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_url = f"mongodb://{user}:{password}@{host}:{port}"
    db_name = os.getenv("DB_SAGA_NAME")
    collection_name = os.getenv("DB_SAGA_COLLECTION_NAME")
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )

    mongodb.connect()

    data = create_random_data()
    data.pop("sagaId")

    valid = mongodb._validator(data=data)
    assert valid is False


def create_random_data():
    random_guildId = ""
    for _ in range(18):
        random_number = randint(0, 10)
        random_guildId += str(random_number)

    data = {
        "choreography": {
            "name": "DISCORD_UPDATE_CHANNELS",
            "transactions": [
                {
                    "queue": "DISCORD_ANALYZER",
                    "event": "RUN",
                    "order": 1,
                    "status": "NOT_STARTED",
                },
            ],
        },
        "status": "NOT_STARTED",
        "data": {"guildId": "sample_guild", "created": True},
        "sagaId": "14497720-1132-11ee-96f6-fd4f90065411",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": (datetime.now() + timedelta(minutes=2)).isoformat(),
    }

    return data
