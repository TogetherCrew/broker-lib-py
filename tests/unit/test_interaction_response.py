from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.attachment import (
    Attachment,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.embed import Embed
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.interaction_callback_data import (
    InteractionCallbackData,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.interaction_response import (
    InteractionResponse,
)


def test_interaction_response_empty_inputs():
    inter_response = InteractionResponse(type=123)

    assert inter_response.type == 123
    assert inter_response.data is None


def test_interaction_response_sample_data():
    embed = Embed(title="Test Embed", description="This is a test")

    attachment = Attachment(id=123, url="https://example.com/test.png")
    components = [
        {
            "type": 1,
            "components": [
                {"type": 2, "label": "Click me!", "style": 1, "custom_id": "click_one"}
            ],
        }
    ]

    data = InteractionCallbackData(
        tts=True,
        content="Test Content",
        embeds=[embed],
        allowed_mentions={"users": ["123456789"]},
        flags=1,
        components=components,
        attachments=[attachment],
    )
    response = InteractionResponse(type=4, data=data)
    assert response.type == 4
    assert isinstance(response.data, InteractionCallbackData)
    assert response.data.tts is True
    assert response.data.content == "Test Content"
    assert len(response.data.embeds) == 1
    assert response.data.embeds[0].title == "Test Embed"
    assert response.data.allowed_mentions == {"users": ["123456789"]}
    assert response.data.flags == 1
    assert len(response.data.components) == 1
    assert len(response.data.components[0]) == 2
    assert response.data.components[0]["components"][0]["type"] == 2
    assert response.data.components[0]["components"][0]["label"] == "Click me!"
    assert response.data.components[0]["components"][0]["style"] == 1
    assert response.data.components[0]["components"][0]["custom_id"] == "click_one"

    assert len(response.data.attachments) == 1
    assert response.data.attachments[0].url == "https://example.com/test.png"


def test_interaction_response_to_dict():
    embed = Embed(title="Test Embed", description="This is a test")

    attachment = Attachment(id=123, url="https://example.com/test.png")
    components = [
        {
            "type": 1,
            "components": [
                {"type": 2, "label": "Click me!", "style": 1, "custom_id": "click_one"}
            ],
        }
    ]

    data = InteractionCallbackData(
        tts=True,
        content="Test Content",
        embeds=[embed],
        allowed_mentions={"users": ["123456789"]},
        flags=1,
        components=components,
        attachments=[attachment],
    )
    response = InteractionResponse(type=4, data=data)

    response_dict = response.to_dict()
    assert response_dict["type"] == 4
    assert isinstance(response_dict["data"], dict)
    assert response_dict["data"]["tts"] is True
    assert response_dict["data"]["content"] == "Test Content"
    assert len(response_dict["data"]["embeds"]) == 1
    assert response_dict["data"]["embeds"][0]["title"] == "Test Embed"
    assert response_dict["data"]["allowed_mentions"] == {"users": ["123456789"]}
    assert response_dict["data"]["flags"] == 1
    assert len(response_dict["data"]["components"]) == 1
    assert len(response_dict["data"]["components"][0]) == 2
    assert response_dict["data"]["components"][0]["components"][0]["type"] == 2
    assert (
        response_dict["data"]["components"][0]["components"][0]["label"] == "Click me!"
    )
    assert response_dict["data"]["components"][0]["components"][0]["style"] == 1
    assert (
        response_dict["data"]["components"][0]["components"][0]["custom_id"]
        == "click_one"
    )

    assert len(response_dict["data"]["attachments"]) == 1
    assert (
        response_dict["data"]["attachments"][0]["url"] == "https://example.com/test.png"
    )


def test_interaction_response_from_dict():
    embed = Embed(title="Test Embed", description="This is a test")

    attachment = Attachment(id=123, url="https://example.com/test.png")
    components = [
        {
            "type": 1,
            "components": [
                {"type": 2, "label": "Click me!", "style": 1, "custom_id": "click_one"}
            ],
        }
    ]

    data = InteractionCallbackData(
        tts=True,
        content="Test Content",
        embeds=[embed],
        allowed_mentions={"users": ["123456789"]},
        flags=1,
        components=components,
        attachments=[attachment],
    )
    response = InteractionResponse(type=4, data=data)

    response_dict = response.to_dict()

    response_from_dict = InteractionResponse.from_dict(response_dict)
    assert response_from_dict.type == 4
    assert isinstance(response_from_dict.data, InteractionCallbackData)
    assert response_from_dict.data.tts is True
    assert response_from_dict.data.content == "Test Content"
    assert len(response_from_dict.data.embeds) == 1
    assert response_from_dict.data.embeds[0].title == "Test Embed"
    assert response_from_dict.data.allowed_mentions == {"users": ["123456789"]}
    assert response_from_dict.data.flags == 1
    assert len(response_from_dict.data.components) == 1
    assert len(response_from_dict.data.components[0]) == 2
    assert response_from_dict.data.components[0]["components"][0]["type"] == 2
    assert (
        response_from_dict.data.components[0]["components"][0]["label"] == "Click me!"
    )
    assert response_from_dict.data.components[0]["components"][0]["style"] == 1
    assert (
        response_from_dict.data.components[0]["components"][0]["custom_id"]
        == "click_one"
    )

    assert len(response_from_dict.data.attachments) == 1
    assert response_from_dict.data.attachments[0].url == "https://example.com/test.png"
