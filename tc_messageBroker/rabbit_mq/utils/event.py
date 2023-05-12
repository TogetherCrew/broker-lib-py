from tc_messageBroker.rabbit_mq.status import Status
from datetime import datetime


class Event:
    """abstract class"""

    def __init__(
        self,
        name: str,
        description: str,
        status: Status,
        message: any,
        start: datetime.timestamp,
        end: datetime.timestamp,
        runtime: int,
        ## type is showing the Exception
        error: type | None,
    ) -> None:
        self.name = name
        self.description = description
        self.status = status
        self.message = message
        self.start = start
        self.end = end
        self.runtime = runtime
        self.error = error
