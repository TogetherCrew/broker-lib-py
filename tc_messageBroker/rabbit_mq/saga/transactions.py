from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.status import Status
from .transaction_base import ITransaction


class DISCORD_UPDATE_CHANNELS_TRANSACTIONS:
    transactions = [
        ITransaction(
            Queue.DISCORD_BOT,
            Event.DISCORD_BOT.FETCH,
            order=1,
            status=Status.NOT_STARTED,
            message=None,
            start=None,
            end=None,
            runtime=None,
            error=None,
        ),
        ITransaction(
            Queue.DISCORD_BOT,
            Event.DISCORD_BOT.FETCH,
            order=2,
            status=Status.NOT_STARTED,
            message=None,
            start=None,
            end=None,
            runtime=None,
            error=None,
        ),
    ]
