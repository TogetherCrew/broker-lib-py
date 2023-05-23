from tc_messageBroker import RabbitMQ
import pytest


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_default_exchange_direct():
    """
    declare direct exchange point with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """

    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point", type="direct")


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_default_exchange_topic():
    """
    declare topic exchange point with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point2", type="topic")


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_exchange_fanout():
    """
    declare fanout exchange point with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point3", type="fanout")


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_default_exchange_headers():
    """
    declare `match` exchange with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point4", type="headers")


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_durable_false_exchange_direct():
    """
    declare `match` exchange with default parameters,
     durable = False,
     auto_delete = False,
     options = None
    """
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(
        name="exchange_point5",
        type="direct",
        durable=False,
    )


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_declare_auto_delete_true_exchange_direct():
    """
    declare `match` exchange with default parameters,
     durable = False,
     auto_delete = False,
     options = None
    """
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(
        name="exchange_point6",
        type="direct",
        auto_delete=True,
    )


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_publish_on_exchange():
    """
    declare direct exchange point with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """

    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point7", type="direct")
    messageBroker.publish_on_exchange(
        exchange_name="exchange_point7",
        routing_key="sample",
        event="test_event",
        content={"guildId": 123},
    )


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no RabbitMQ instance available)"
)
def test_tc_message_broker_bind_queue_on_exchange():
    """
    declare direct exchange point with default parameters,
     durable = True,
     auto_delete = False,
     options = None
    """

    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)
    _ = messageBroker.connect(queue_name="test_queue")

    messageBroker.create_exchange(name="exchange_point8", type="direct")

    messageBroker.bind_queue_to_exchange(
        queue_name="sample_queue", exchange_name="exchange_point8", pattern="sample"
    )
