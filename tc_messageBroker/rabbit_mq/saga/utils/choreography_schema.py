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
                    "type": "object",
                    "patternProperties": {
                        "^[0-9]+$": {
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
                                "start": {"type": "string"},
                                "end": {"type": "string"},
                                "runtime": {"type": "number"},
                                "error": {"type": "string"},
                            },
                            "required": ["queue", "event", "order", "status"],
                            "additionalProperties": False,
                        }
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
        "createdAt": {"type": "string", "format": "date-time"},
        "updatedAt": {"type": "string", "format": "date-time"},
    },
    "required": ["sagaId", "choreography", "status", "createdAt", "updatedAt"],
    "additionalProperties": False,
}
