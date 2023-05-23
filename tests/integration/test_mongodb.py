from tc_messageBroker.rabbit_mq.db_operations import MongoDB
from uuid import uuid1
from numpy.random import randint
from copy import deepcopy
from datetime import datetime, timedelta
import pytest


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_insert_one():
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    data = create_random_data()

    mongodb.write(data=[data])


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_insert_multiple():
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    documents = []
    for _ in range(5):
        data = create_random_data()
        documents.append(data)

    mongodb.write(data=documents)


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_read_count_one():
    """
    read from db after writing using the previous function (above)
    """
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    results = mongodb.read(query={}, count=1)

    assert isinstance(results, dict) is True
    assert "choreography" in results.keys()
    assert "status" in results.keys()
    assert "data" in results.keys()
    assert "sagaId" in results.keys()
    assert "createdAt" in results.keys()
    assert "updatedAt" in results.keys()


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_read_count_multiple():
    """
    read from db after writing using the previous function (above)
    """
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    data_count = 5
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


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_replace():
    """
    test replacing a document we just inserted
    """
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    data = create_random_data()

    mongodb.write(data=[data])

    data.pop("_id")

    new_data = deepcopy(data)

    choreography_name = "NEW_TEST"
    tx_state = "SUCCESS"

    new_data["choreography"]["name"] = choreography_name
    new_data["choreography"]["name"] = choreography_name
    new_data["choreography"]["transactions"]["0"]["status"] = tx_state

    mongodb.replace(data["sagaId"], new_data)

    document = mongodb.read({"sagaId": new_data["sagaId"]})
    document.pop("_id")

    assert document != data
    assert document == new_data


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_delete():
    """
    delete all except one of the ligitimate data which we choose
    """

    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    mongodb.delete(query={"data.guildId": {"$ne": "993163081939165234"}})


@pytest.mark.skip(reason="No MongoDB instance available.")
def test_wrong_input():
    """
    give wrong input to insert
    """
    connection_url = "mongodb://127.0.0.1:27017/"

    mongodb = MongoDB(connection_str=connection_url)
    mongodb.connect()

    data = create_random_data()
    data.pop("sagaId")

    valid = mongodb._validator(data=data)
    assert valid is False


@pytest.mark.skip(reason="No MongoDB instance available.")
def create_random_data():
    random_guildId = ""
    for _ in range(18):
        random_number = randint(0, 10)
        random_guildId += str(random_number)

    data = {
        "choreography": {
            "name": f"test_{randint(0, 50)}",
            "transactions": {
                "0": {
                    "queue": "SERVER_API",
                    "event": "UPDATE_GUILD",
                    "order": 1,
                    "status": "NOT_STARTED",
                },
                "1": {
                    "queue": "DISCORD_BOT",
                    "event": "SEND_MESSAGE",
                    "order": 2,
                    "status": "NOT_STARTED",
                },
            },
        },
        "status": "NOT_STARTED",
        "data": {"guildId": random_guildId},
        "sagaId": str(uuid1()),
        "createdAt": datetime.now().isoformat(),
        "updatedAt": (datetime.now() + timedelta(minutes=2)).isoformat(),
    }

    return data
