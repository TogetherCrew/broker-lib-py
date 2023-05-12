from enum import Enum


class Status(Enum):
    PENDING = 0
    IN_PROGRESS = 1
    SUCCESS = 2
    FAILED = 3
    CANCELLED = 4
