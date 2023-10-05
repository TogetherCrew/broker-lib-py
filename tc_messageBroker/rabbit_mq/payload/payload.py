from .payload_microservices import (
    DiscordInteractionResponsePayload,
    DiscordFollowUpMessage,
)


class DiscordPayload:
    INTERACTION_RESPONSE = DiscordInteractionResponsePayload
    FOLLOWUP_MESSAGE = DiscordFollowUpMessage


class Payload:
    DISCORD_BOT = DiscordPayload
