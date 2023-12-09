from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
import asyncio


async def job(broker_url, port, username, password):
    rabbit_mq = RabbitMQ(
        broker_url=broker_url, port=port, username=username, password=password
    )

    content = {"uuid": "d99a1490-fba6-11ed-b9a9-0d29e7612dp8", "data": "some results"}

    await rabbit_mq.connect_async(Queue.DISCORD_BOT)
    await rabbit_mq.publish_async(
        Queue.DISCORD_ANALYZER,
        event=Event.DISCORD_ANALYZER.RUN,
        content=content,
    )


if __name__ == "__main__":
    broker_url = "localhost"
    port = 5672
    username = "guest"
    password = "guest"

    asyncio.run(job(broker_url, port, username, password))
