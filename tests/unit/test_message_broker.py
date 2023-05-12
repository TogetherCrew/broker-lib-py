from tc_messageBroker import TC_message_broker


def test_tc_message_broker_default_mode():
    url = "localhost"
    messageBroker = TC_message_broker(broker_url=url)

    assert messageBroker.broker_url == url


def test_tc_message_broker_empty_url():
    url = ""
    messageBroker = TC_message_broker(broker_url=url)

    assert messageBroker.broker_url == url


def test_tc_message_broker_singleton():
    url = "localhost"

    messageBroker = TC_message_broker(broker_url=url)

    assert messageBroker.broker_url == url

    url_new = "127.0.0.1"
    messageBroker2 = TC_message_broker(broker_url=url_new)

    assert messageBroker == messageBroker2
    assert messageBroker.broker_url == url_new
    assert messageBroker2.broker_url == url_new
