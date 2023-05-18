from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.status import Status
from .transaction_base import ITransaction


class DISCORD_UPDATE_CHANNELS_TRANSACTIONS(ITransaction):
    def __init__(self) -> None:
        super().__init__(
            Queue.DISCORD_BOT,
            Event.DISCORD_BOT.FETCH,
            order=1,
            status=Status.PENDING,
            message=None,
            start=None,
            end=None,
            runtime=None,
            error=None,
        )
