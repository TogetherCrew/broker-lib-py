from .payload_microservices import (
    DiscordFollowUpMessage,
    DiscordInteractionResponsePayload,
)


class DiscordPayload:
    INTERACTION_RESPONSE = DiscordInteractionResponsePayload
    FOLLOWUP_MESSAGE = DiscordFollowUpMessage


class Payload:
    DISCORD_BOT = DiscordPayload
