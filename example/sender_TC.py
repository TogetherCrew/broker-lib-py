from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue


if __name__ == "__main__":
    broker_url = "localhost"
    rabbit_mq = RabbitMQ(broker_url=broker_url)

    rabbit_mq.connect(Queue.DISCORD_ANALYZER)

    content = {"content": "content_analyzer_publish"}

    rabbit_mq.publish(
        Queue.DISCORD_ANALYZER, event=Event.DISCORD_ANALYZER.RUN, content=content
    )
