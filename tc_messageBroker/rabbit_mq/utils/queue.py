from tc_messageBroker.rabbit_mq.utils.event import Event


class Queue:
    """abstract class"""

    def __init__(self, name: str, description: str, events: dict[any, Event]) -> None:
        self.name = name
        self.description = description
        self.events = events
