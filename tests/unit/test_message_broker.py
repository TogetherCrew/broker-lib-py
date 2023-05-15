from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.event import Event


def test_tc_message_broker_default_mode():
    url = "localhost"
    messageBroker = RabbitMQ(broker_url=url)

    assert messageBroker.broker_url == url


def test_tc_message_broker_empty_url():
    url = ""
    messageBroker = RabbitMQ(broker_url=url)

    assert messageBroker.broker_url == url


def test_tc_message_broker_singleton():
    url = "localhost"

    messageBroker = RabbitMQ(broker_url=url)

    assert messageBroker.broker_url == url

    url_new = "127.0.0.1"
    messageBroker2 = RabbitMQ(broker_url=url_new)

    assert messageBroker == messageBroker2
    assert messageBroker.broker_url == url_new
    assert messageBroker2.broker_url == url_new


def test_connection_rabbit_mq():
    broker_url = "localhost"

    rabbit_mq = RabbitMQ(broker_url=broker_url)
    success = rabbit_mq.connect("test_queue")
    rabbit_mq.connection.close()

    assert success is True


def test_consume_publish_no_event():
    """
    consume an event which does not exists
    """
    broker_url = "localhost"

    rabbit_mq = RabbitMQ(broker_url=broker_url)
    rabbit_mq.connect(Queue.DISCORD_ANALYZER)

    content = {"content": "content_analyzer_publish"}

    rabbit_mq.publish(
        queue_name=Queue.DISCORD_ANALYZER,
        event=Event.DISCORD_ANALYZER.RUN,
        content=content,
    )
    rabbit_mq.consume(Queue.DISCORD_ANALYZER)
    rabbit_mq.connection.close()


# def test_consume_publish_with_event():
#     """
#     consume an event which does not exists
#     """
#     broker_url = 'localhost'

#     rabbit_mq = RabbitMQ(broker_url=broker_url)
#     rabbit_mq.connect(Queue.DISCORD_ANALYZER)

#     content = {
#         'content': 'content_analyzer_publish'
#     }

#     global_var = None

#     def event_function():
#         global global_var
#         global rabbit_mq
#         global_var = True

#         # rabbit_mq.channel.stop_consuming(consumer_tag='SAMPLE')

#     rabbit_mq.publish(
#         Queue.DISCORD_ANALYZER,
#         Event.DISCORD_ANALYZER.RUN,
#         content=content
#     )
#     rabbit_mq.consume(
#         Queue.DISCORD_ANALYZER, 
#         consume_options={'consumer_tag': 'SAMPLE'}
#     )
#    rabbit_mq.channel.basic_consume(
#        Queue.DISCORD_ANALYZER, 
#        rabbit_mq._consume_callback
#    )

#     rabbit_mq.channel.start_consuming()

#     rabbit_mq.connection.close()

#     assert global_var == True
