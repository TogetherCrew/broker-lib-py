from .discord_bot.interaction_response import InteractionResponse
from .discord_bot.chat_input_interaction import ChatInputCommandInteraction
from .discord_bot.base_types.interaction_callback_data import InteractionCallbackData


class DiscordBotInteractionResponseCreatePayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
        interaction_response: InteractionResponse | None = None,
    ) -> None:
        self.type = None
        self.data = None
        if interaction is not None:
            self.type = interaction_response.type
            self.data = interaction_response.data

        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseCreatePayload":
        interaction = d.get("interaction")
        data = d.get("data")
        type = d.get("type")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(interaction)

        interaction_response = InteractionResponse.from_dict(
            {"type": type, "data": data}
        )

        return cls(
            interaction=interaction,
            interaction_response=interaction_response,
        )

    def to_dict(self):
        return {"type": self.type, "data": self.data, "interaction": self.interaction}


class DiscordBotInteractionResponseEditPayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
        data: InteractionCallbackData | None = None,
    ) -> None:
        self.data = data
        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseEditPayload":
        interaction = d.get("interaction")
        data = d.get("data")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(interaction)

        data = InteractionCallbackData.from_dict(data)

        return cls(interaction=interaction, data=data)

    def to_dict(self):
        return {"data": self.data, "interaction": self.interaction}


class DiscordBotInteractionResponseDeletePayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
    ) -> None:
        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseDeletePayload":
        interaction = d.get("interaction")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(interaction)

        return cls(interaction=interaction)

    def to_dict(self):
        return {"interaction": self.interaction}


class DiscordInteractionResponsePayload:
    Create = DiscordBotInteractionResponseCreatePayload
    Edit = DiscordBotInteractionResponseEditPayload
    Delete = DiscordBotInteractionResponseDeletePayload


class DiscordFollowUpMessage:
    Create = DiscordBotInteractionResponseEditPayload
