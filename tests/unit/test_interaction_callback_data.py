from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.attachment import (
    Attachment,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.embed import Embed
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.interaction_callback_data import (
    InteractionCallbackData,
)


def test_interaction_callback_data_empty_data():
    # Test creating an empty InteractionCallbackData object
    data = InteractionCallbackData()
    assert data.tts is None
    assert data.content is None
    assert data.embeds is None
    assert data.allowed_mentions is None
    assert data.flags is None
    assert data.components is None
    assert data.attachments is None


def test_interaction_callback_data_some_data():
    # Test creating an InteractionCallbackData object with all fields
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
    assert data.tts is True
    assert data.content == "Test Content"
    assert len(data.embeds) == 1
    assert data.embeds[0].title == "Test Embed"
    assert data.allowed_mentions == {"users": ["123456789"]}
    assert data.flags == 1

    assert len(data.components) == 1
    assert data.components[0]["type"] == 1
    assert data.components[0]["components"][0]["type"] == 2
    assert data.components[0]["components"][0]["label"] == "Click me!"
    assert data.components[0]["components"][0]["style"] == 1
    assert data.components[0]["components"][0]["custom_id"] == "click_one"

    assert len(data.attachments) == 1
    assert data.attachments[0].url == "https://example.com/test.png"


def test_interaction_callback_data_to_dict():
    # Test converting to and from a dictionary
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

    data_dict = data.to_dict()
    assert data_dict["tts"] is True
    assert data_dict["content"] == "Test Content"
    assert len(data_dict["embeds"]) == 1
    assert data_dict["embeds"][0]["title"] == "Test Embed"
    assert data_dict["allowed_mentions"] == {"users": ["123456789"]}
    assert data_dict["flags"] == 1

    assert len(data_dict["components"]) == 1
    assert data_dict["components"][0]["type"] == 1
    assert data_dict["components"][0]["components"][0]["type"] == 2
    assert data_dict["components"][0]["components"][0]["label"] == "Click me!"
    assert data_dict["components"][0]["components"][0]["style"] == 1
    assert data_dict["components"][0]["components"][0]["custom_id"] == "click_one"

    assert len(data_dict["attachments"]) == 1
    assert data_dict["attachments"][0]["url"] == "https://example.com/test.png"


def test_interaction_callback_data_from_dict():
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

    data_dict = data.to_dict()
    data_from_dict = InteractionCallbackData.from_dict(data_dict)
    assert data_from_dict.tts is True
    assert data_from_dict.content == "Test Content"
    assert len(data_from_dict.embeds) == 1
    assert data_from_dict.embeds[0].title == "Test Embed"
    assert data_from_dict.allowed_mentions == {"users": ["123456789"]}
    assert data_from_dict.flags == 1
    assert len(data_from_dict.components) == 1
    assert data_from_dict.components[0]["type"] == 1
    assert data_from_dict.components[0]["components"][0]["type"] == 2
    assert data_from_dict.components[0]["components"][0]["label"] == "Click me!"
    assert data_from_dict.components[0]["components"][0]["style"] == 1
    assert data_from_dict.components[0]["components"][0]["custom_id"] == "click_one"
    assert len(data_from_dict.attachments) == 1
    assert data_from_dict.attachments[0].url == "https://example.com/test.png"
