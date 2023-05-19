from uuid import uuid1
from tc_messageBroker.rabbit_mq.status import Status

choreography_schema = {
    "sagaId": {"type": "string", "required": True, "unique": True, "default": uuid1()},
    "choreography": {
        "name": {
            "type": "string",
            "required": True,
        },
        "transactions": {
            "queue": {"type": "string", "required": True},
            "event": {"type": "string", "required": True},
            "order": {"type": "number", "required": True},
            "status": {
                "type": "string",
                "required": True,
                "enum": [
                    Status.NOT_STARTED,
                    Status.IN_PROGRESS,
                    Status.SUCCESS,
                    Status.FAILED,
                    Status.CANCELLED,
                ],
            },
            "message": {"type": "string", "required": False},
            "start": {"type": "date-time", "required": False},
            "end": {"type": "date-time", "required": False},
            "runtime": {"type": "number", "required": False},
            "error": {"type": "string", "required": False},
        },
    },
    "status": {
        "type": "string",
        "enum": [
            Status.NOT_STARTED,
            Status.IN_PROGRESS,
            Status.SUCCESS,
            Status.FAILED,
            Status.CANCELLED,
        ],
        "required": True,
    },
    "data": {"type": "dict", "required": False},
    "createdAt": {"type": "date-time", "required": True},
    "updatedAt": {"type": "date-time", "required": True},
}
