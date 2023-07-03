from tc_messageBroker import RabbitMQ


def test_queue_declare_empty_params():
    url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )
    kwargs = {}
    (
        queue_durability, 
        queue_auto_delete
    ) = messageBroker._get_declare_queue_param(kwargs)
    
    assert queue_durability == True
    assert queue_auto_delete == False

def test_queue_declare_auto_delete_params():
    url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )

    kwargs = {
        "queue_auto_delete": True
    }

    (
        queue_durability, 
        queue_auto_delete
    ) = messageBroker._get_declare_queue_param(kwargs)
    
    assert queue_durability == True
    assert queue_auto_delete == True

def test_queue_declare_all_params():
    url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )

    kwargs = {
        "queue_auto_delete": True,
        "queue_durable": False
    }

    (
        queue_durability, 
        queue_auto_delete
    ) = messageBroker._get_declare_queue_param(kwargs)
    
    assert queue_durability == False
    assert queue_auto_delete == True


def test_queue_declare_all_params_second():
    url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )

    kwargs = {
        "queue_auto_delete": False,
        "queue_durable": False
    }

    (
        queue_durability, 
        queue_auto_delete
    ) = messageBroker._get_declare_queue_param(kwargs)
    
    assert queue_durability == False
    assert queue_auto_delete == False



