from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.status import Status
from .transaction_base import ITransaction


DISCORD_UPDATE_CHANNELS_TRANSACTIONS = [
    ITransaction(
        Queue.DISCORD_BOT,
        Event.DISCORD_BOT.FETCH,
        order=1,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.DISCORD_ANALYZER,
        Event.DISCORD_ANALYZER.RUN,
        order=2,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.DISCORD_ANALYZER,
        Event.DISCORD_ANALYZER.SAVE,
        order=3,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.SERVER_API,
        Event.SERVER_API.UPDATE_GUILD,
        order=4,
        status=Status.NOT_STARTED,
    ),
]
