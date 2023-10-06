from .base_types.interaction_callback_data import InteractionCallbackData


class InteractionResponse:
    def __init__(self, type: int, data: InteractionCallbackData | None = None) -> None:
        self.type = type
        self.data = data

    @classmethod
    def from_dict(cls, d: dict) -> "InteractionResponse":
        data = d.get("data")
        if data is not None:
            data = InteractionCallbackData.from_dict(data)

        return cls(type=d["type"], data=data)

    def to_dict(self) -> dict:
        type = self.type
        data = self.data

        if data is not None:
            data = data.to_dict()

        return {"type": type, "data": data}
