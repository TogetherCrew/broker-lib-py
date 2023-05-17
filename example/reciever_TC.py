from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue


def do_something():
    A = 2 * 2
    message = f"Calculation Results: {A}"
    print(message)


if __name__ == "__main__":
    broker_url = "localhost"
    rabbit_mq = RabbitMQ(broker_url=broker_url)

    rabbit_mq.on_event(Event.DISCORD_ANALYZER.RUN, do_something)

    rabbit_mq.connect(Queue.DISCORD_ANALYZER)

    rabbit_mq.consume(Queue.DISCORD_ANALYZER)
    rabbit_mq.channel.start_consuming()
