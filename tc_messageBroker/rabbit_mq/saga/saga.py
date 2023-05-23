from .choreography import ChoreographyDict
from .saga_base import Saga
from tc_messageBroker.rabbit_mq.status import Status
from datetime import datetime


class DiscordUpdateChannel(Saga):
    def __init__(self, data: any) -> None:
        super().__init__(
            ChoreographyDict.DISCORD_UPDATE_CHANNELS,
            Status.NOT_STARTED,
            data=data,
            created_at=datetime.now(),
            next=None,
        )
