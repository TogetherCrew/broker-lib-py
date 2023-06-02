from tc_messageBroker.rabbit_mq.status import Status

choreography_schema = {
    "type": "object",
    "properties": {
        "sagaId": {"type": "string", "unique": True},
        "choreography": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                },
                "transactions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "queue": {"type": "string"},
                            "event": {"type": "string"},
                            "order": {"type": ["integer", "string"]},
                            "status": {
                                "type": "string",
                                "enum": [
                                    Status.NOT_STARTED,
                                    Status.IN_PROGRESS,
                                    Status.SUCCESS,
                                    Status.FAILED,
                                    Status.CANCELLED,
                                ],
                            },
                            "message": {"type": "string"},
                            "start": {},
                            "end": {},
                            "runtime": {"type": "number"},
                            "error": {"type": "string"},
                        },
                        "required": ["queue", "event", "order", "status"],
                        "additionalProperties": False,
                    },
                    "additionalProperties": False,
                },
            },
            "required": ["name", "transactions"],
            "additionalProperties": False,
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
        },
        "data": {"type": "object"},
        "createdAt": {},
        "updatedAt": {},
    },
    "required": ["sagaId", "choreography", "status", "createdAt", "updatedAt"],
    "additionalProperties": False,
}
