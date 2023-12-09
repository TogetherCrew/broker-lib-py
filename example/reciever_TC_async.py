import asyncio

from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue


def do_something(recieved_data):
    A = 2 * 2
    message = f"Calculation Results: {A}"
    print(message)
    print(f"recieved_data: {recieved_data}")


async def job(broker_url, port, username, password):
    rabbit_mq = RabbitMQ(
        broker_url=broker_url, port=port, username=username, password=password
    )

    await rabbit_mq.on_event_async(Event.DISCORD_ANALYZER.RUN, do_something)
    await rabbit_mq.connect_async(Queue.DISCORD_ANALYZER)
    await rabbit_mq.consume_async(Queue.DISCORD_ANALYZER)

    if rabbit_mq.channel is not None:
        rabbit_mq.channel.start_consuming()
    else:
        print("Connection to broker was not successful!")


if __name__ == "__main__":
    broker_url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    asyncio.run(job(broker_url, port, username, password))
