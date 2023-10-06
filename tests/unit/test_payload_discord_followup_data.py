import unittest

from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.allowed_mentions import (
    AllowedMentions,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.attachment import (
    Attachment,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.create_followup_message_data import (
    FollowUpMessageData,
)


class TestDiscordMessage(unittest.TestCase):
    def test_param_setting_empty_all(self):
        message = FollowUpMessageData()
        assert message.content is None
        assert message.username is None
        assert message.avatar_url is None
        assert message.tts is None
        assert message.embeds is None
        assert message.allowed_mentions is None
        assert message.components is None
        assert message.files is None
        assert message.payload_json is None
        assert message.flags is None
        assert message.thread_name is None

    def test_param_setting_all_inputs_set(self):
        allowed_mention = AllowedMentions()
        message_component = [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "Click me!",
                        "style": 1,
                        "custom_id": "click_one",
                    }
                ],
            }
        ]
        attachment = Attachment(id=123)

        message = FollowUpMessageData(
            content="Hello world!",
            username="TestUser",
            avatar_url="https://example.com/avatar.png",
            tts=True,
            embeds=[],
            allowed_mentions=allowed_mention,
            components=message_component,
            files=[{"file1": "sample"}],
            payload_json="{payload: 1}",
            attachments=attachment,
            flags=0,
            thread_name="general",
        )
        self.assertEqual(message.content, "Hello world!")
        self.assertEqual(message.username, "TestUser")
        self.assertEqual(message.avatar_url, "https://example.com/avatar.png")
        self.assertEqual(message.tts, True)
        self.assertEqual(message.embeds, [])
        self.assertEqual(message.allowed_mentions, allowed_mention)
        self.assertEqual(message.components, message_component)
        self.assertEqual(message.files, [{"file1": "sample"}])
        self.assertEqual(message.payload_json, "{payload: 1}")
        self.assertEqual(message.flags, 0)
        self.assertEqual(message.thread_name, "general")

    def test_to_dict(self):
        message = FollowUpMessageData(
            content="Hello world!",
            username="TestUser",
            avatar_url="https://example.com/avatar.png",
            tts=True,
            embeds=[],
            allowed_mentions=None,
            components=None,
            files=None,
            payload_json=None,
            attachments=None,
            flags=None,
            thread_name=None,
        )
        expected_dict = {
            "content": "Hello world!",
            "username": "TestUser",
            "avatar_url": "https://example.com/avatar.png",
            "tts": True,
            "embeds": [],
        }
        self.assertEqual(message.to_dict(), expected_dict)

    def test_from_dict(self):
        message_dict = {
            "content": "Hello world!",
            "username": "TestUser",
            "avatar_url": "https://example.com/avatar.png",
            "tts": True,
            "embeds": [],
        }
        expected_message = FollowUpMessageData(
            content="Hello world!",
            username="TestUser",
            avatar_url="https://example.com/avatar.png",
            tts=True,
            embeds=[],
            allowed_mentions=None,
            components=None,
            files=None,
            payload_json=None,
            attachments=None,
            flags=None,
            thread_name=None,
        )
        self.assertEqual(
            FollowUpMessageData.from_dict(message_dict).__dict__,
            expected_message.__dict__,
        )
