from .choreography import ChoreographyDict
from .saga_base import ISaga
from tc_messageBroker.rabbit_mq.status import Status
from datetime import datetime


class DiscordUpdateChannel(ISaga):
    def __init__(self, data: any) -> None:
        super().__init__(
            ChoreographyDict.DISCORD_UPDATE_CHANNELS,
            Status.NOT_STARTED,
            data=data,
            created_at=datetime.now(),
            next=None,
        )
