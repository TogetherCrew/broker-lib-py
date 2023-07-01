from tc_messageBroker.rabbit_mq.db_operations.mongodb import MongoDB


def test_mongo_class():
    connection_url = "connection_str"
    db_name = "Sagas"
    collection_name = "saga"
    mongodb = MongoDB(
        connection_str=connection_url, db_name=db_name, collection_name=collection_name
    )

    assert mongodb.connection_str == connection_url
    assert mongodb.db_name == db_name
    assert mongodb.collection_name == collection_name
    assert mongodb.client is None
