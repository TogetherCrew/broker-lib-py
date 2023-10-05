from tc_messageBroker.rabbit_mq.payload.payload import Payload
from tc_messageBroker.rabbit_mq.payload.payload_microservices import (
    DiscordBotFollowUpMessageCreatePayload,
    DiscordBotInteractionResponseCreatePayload,
    DiscordBotInteractionResponseDeletePayload,
    DiscordBotInteractionResponseEditPayload,
)


def test_available_payloads():
    """
    test if we had chosen the righ alias names
    """
    assert (
        Payload.DISCORD_BOT.INTERACTION_RESPONSE.Create
        == DiscordBotInteractionResponseCreatePayload
    )
    assert (
        Payload.DISCORD_BOT.INTERACTION_RESPONSE.Edit
        == DiscordBotInteractionResponseEditPayload
    )
    assert (
        Payload.DISCORD_BOT.INTERACTION_RESPONSE.Delete
        == DiscordBotInteractionResponseDeletePayload
    )
    assert (
        Payload.DISCORD_BOT.FOLLOWUP_MESSAGE.Create
        == DiscordBotFollowUpMessageCreatePayload
    )
