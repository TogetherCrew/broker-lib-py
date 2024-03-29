from .discord_bot.chat_input_interaction import ChatInputCommandInteraction
from .discord_bot.create_followup_message_data import FollowUpMessageData
from .discord_bot.edit_webhook_data import InteractionResponseEditData
from .discord_bot.interaction_response import InteractionResponse


class DiscordBotInteractionResponseCreatePayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
        data: InteractionResponse | None = None,
    ) -> None:
        """
        to set right values please refer to
        https://discord.com/developers/docs/interactions/receiving-and-responding#create-interaction-response
        """
        self.data = data
        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseCreatePayload":
        interaction = d.get("interaction")
        data = d.get("data")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(interaction)

        if data is not None:
            data = InteractionResponse.from_dict(data)

        return cls(
            data=data,
            interaction=interaction,
        )

    def to_dict(self):
        return {"data": self.data.to_dict(), "interaction": self.interaction.to_dict()}


class DiscordBotInteractionResponseEditPayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
        data: InteractionResponseEditData | None = None,
    ) -> None:
        """
        to set the right values please refer to
        https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response
        """
        self.data = data
        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseEditPayload":
        interaction = d.get("interaction")
        data = d.get("data")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(
                interaction
            )  # type: ignore

        data = InteractionResponseEditData.from_dict(data)  # type: ignore

        return cls(interaction=interaction, data=data)

    def to_dict(self):
        return {"data": self.data.to_dict(), "interaction": self.interaction.to_dict()}


class DiscordBotInteractionResponseDeletePayload:
    def __init__(
        self,
        interaction: ChatInputCommandInteraction | None = None,
    ) -> None:
        """
        to set the values right please refer to
        https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response
        """
        self.interaction = interaction

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotInteractionResponseDeletePayload":
        interaction = d.get("interaction")

        if interaction is not None:
            interaction = ChatInputCommandInteraction.from_dict(interaction)

        return cls(interaction=interaction)

    def to_dict(self):
        return {"interaction": self.interaction.to_dict()}


class DiscordBotFollowUpMessageCreatePayload:
    def __init__(
        self, interaction: ChatInputCommandInteraction, data: FollowUpMessageData
    ) -> None:
        """
        to set the values right please refer to
        https://discord.com/developers/docs/interactions/receiving-and-responding#create-followup-message
        """
        self.interaction = interaction
        self.data = data

    @classmethod
    def from_dict(cls, d: dict) -> "DiscordBotFollowUpMessageCreatePayload":
        interaction = d.get("interaction")
        data = d.get("data")

        if interaction:
            interaction = ChatInputCommandInteraction.from_dict(interaction)
        if data:
            data = FollowUpMessageData.from_dict(data)

        return cls(interaction=interaction, data=data)

    def to_dict(self):
        return {"interaction": self.interaction.to_dict(), "data": self.data.to_dict()}


class DiscordInteractionResponsePayload:
    Create = DiscordBotInteractionResponseCreatePayload
    Edit = DiscordBotInteractionResponseEditPayload
    Delete = DiscordBotInteractionResponseDeletePayload


class DiscordFollowUpMessage:
    Create = DiscordBotFollowUpMessageCreatePayload
