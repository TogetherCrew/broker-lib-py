import os

import pytest
from dotenv import load_dotenv
from tc_messageBroker import RabbitMQ


def test_message_broker_connection_singleton():
    """
    test if the singlton class of message broker is the same
    meaning if we connect one class instance the other one should
    be connected by default
    """
    load_dotenv()

    url = os.getenv("RABBIT_HOST")
    port = os.getenv("RABBIT_PORT")
    username = os.getenv("RABBIT_USER")
    password = os.getenv("RABBIT_PASSWORD")

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )
    messageBroker.connect(queue_name="sample_queue")

    assert messageBroker.broker_url == url

    messageBroker2 = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )

    # if error then the class instance is not singleton
    content = {"uuid": "uuid", "data": "some results"}

    messageBroker2.publish(
        queue_name="sample_queue", event="sample_event", content=content
    )


@pytest.mark.asyncio
async def test_message_broker_async_connection_singleton():
    """
    test if the singlton class of message broker is the same
    meaning if we connect one class instance the other one should
    be connected by default
    """
    load_dotenv()

    url = os.getenv("RABBIT_HOST")
    port = os.getenv("RABBIT_PORT")
    username = os.getenv("RABBIT_USER")
    password = os.getenv("RABBIT_PASSWORD")

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )
    await messageBroker.connect_async(queue_name="sample_queue")

    assert messageBroker.broker_url == url

    messageBroker2 = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )

    # if error then the class instance is not singleton
    content = {"uuid": "uuid", "data": "some results"}

    await messageBroker2.publish_async(
        queue_name="sample_queue", event="sample_event", content=content
    )


@pytest.mark.asyncio
async def test_message_broker_async_consume():
    """
    test if the singlton class of message broker is the same
    meaning if we connect one class instance the other one should
    be connected by default
    """
    load_dotenv()

    url = os.getenv("RABBIT_HOST")
    port = os.getenv("RABBIT_PORT")
    username = os.getenv("RABBIT_USER")
    password = os.getenv("RABBIT_PASSWORD")

    messageBroker = RabbitMQ(
        broker_url=url, port=port, username=username, password=password
    )
    await messageBroker.on_event_async(
        "test_event", lambda income_data: print(income_data, 2 * 2)
    )
    await messageBroker.connect_async(queue_name="sample_queue")

    assert messageBroker.broker_url == url

    await messageBroker.consume_async("sample_queue")
