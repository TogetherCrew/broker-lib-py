from datetime import datetime
from typing import Any

from tc_messageBroker.rabbit_mq.status import Status

from .choreography import ChoreographyDict
from .saga_base import Saga


class DiscordUpdateChannel(Saga):
    def __init__(self, data: Any) -> None:
        super().__init__(
            ChoreographyDict.DISCORD_UPDATE_CHANNELS,
            Status.NOT_STARTED,
            data=data,
            created_at=datetime.now(),
        )


class DiscordScheculedJob(Saga):
    def __init__(self, data: Any) -> None:
        super().__init__(
            ChoreographyDict.DISCORD_SCHEDULED_JOB,
            Status.NOT_STARTED,
            data=data,
            created_at=datetime.now(),
        )


class TwitterRefresh(Saga):
    def __init__(self, data: Any) -> None:
        super().__init__(
            ChoreographyDict.TWITTER_REFRESH,
            Status.NOT_STARTED,
            data=data,
            created_at=datetime.now(),
        )
