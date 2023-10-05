import unittest
from datetime import datetime

from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.guild import Guild
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.member import Member


class TestMember(unittest.TestCase):
    def setUp(self):
        guild = Guild(
            id="123",
            name="Test Guild",
            icon="icon.png",
            features=[],
            available=True,
            shard_id=1,
            splash="splash.png",
            banner="banner.png",
            description="Test Description",
            verification_level=2,
            vanity_url_code="test",
            nsfw_level=1,
            premium_subscription_count=0,
            discovery_splash="discovery_splash.png",
            member_count=10,
            large=False,
            premium_progress_bar_enabled=False,
            application_id="456",
            afk_timeout=300,
            afk_channel_id="789",
            system_channel_id="987",
            premium_tier=0,
            widget_enabled=False,
            widget_channel_id="654",
            explicit_content_filter=2,
            mfa_level=1,
            joined_timestamp=int(datetime.now().timestamp()),
            default_message_notifications=1,
            maximum_members=100,
            max_video_channel_users=10,
            max_stage_video_channel_users=5,
            approximate_member_count=10,
            approximate_presence_count=5,
            vanity_url_uses=5,
            rules_channel_id="321",
            public_updates_channel_id="654",
            preferred_locale="en-US",
            safety_alerts_channel_id="987",
            owner_id="123",
        )
        self.member = Member(
            guild=guild,
            joined_timestamp=int(datetime.now().timestamp()),
            premium_since_timestamp=int(datetime.now().timestamp()),
            nickname="Test Member",
            pending=False,
            communication_disabled_until_timestamp=None,
            avatar="avatar.png",
            flags=0,
        )

    def test_member_has_guild(self):
        self.assertIsInstance(self.member.guild, Guild)

    def test_member_has_joined_timestamp(self):
        self.assertIsInstance(self.member.joined_timestamp, int)

    def test_member_has_premium_since_timestamp(self):
        self.assertIsInstance(self.member.premium_since_timestamp, int)

    def test_member_has_nickname(self):
        self.assertIsInstance(self.member.nickname, str)

    def test_member_has_pending(self):
        self.assertIsInstance(self.member.pending, bool)

    def test_member_has_communication_disabled_until_timestamp(self):
        self.assertIsInstance(
            self.member.communication_disabled_until_timestamp, (int, type(None))
        )

    def test_member_has_avatar(self):
        self.assertIsInstance(self.member.avatar, str)

    def test_member_has_flags(self):
        self.assertIsInstance(self.member.flags, int)
