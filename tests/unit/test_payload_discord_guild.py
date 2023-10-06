import unittest

from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.guild import Guild


class TestGuild(unittest.TestCase):
    def test_guild_creation(self):
        guild = Guild(
            id="123",
            name="Test Guild",
            icon=None,
            features=["FEATURE_1", "FEATURE_2"],
            available=True,
            shard_id=1,
            splash=None,
            banner=None,
            description=None,
            verification_level=2,
            vanity_url_code=None,
            nsfw_level=1,
            premium_subscription_count=5,
            discovery_splash=None,
            member_count=50,
            large=False,
            premium_progress_bar_enabled=True,
            application_id=None,
            afk_timeout=300,
            afk_channel_id=None,
            system_channel_id=None,
            premium_tier=3,
            widget_enabled=None,
            widget_channel_id=None,
            explicit_content_filter=2,
            mfa_level=1,
            joined_timestamp=1624914000,
            default_message_notifications=1,
            maximum_members=100,
            max_video_channel_users=10,
            max_stage_video_channel_users=5,
            approximate_member_count=None,
            approximate_presence_count=None,
            vanity_url_uses=None,
            rules_channel_id=None,
            public_updates_channel_id=None,
            preferred_locale="en-US",
            safety_alerts_channel_id=None,
            owner_id="456",
        )

        self.assertEqual(guild.id, "123")
        self.assertEqual(guild.name, "Test Guild")
        self.assertIsNone(guild.icon)
        self.assertListEqual(guild.features, ["FEATURE_1", "FEATURE_2"])
        self.assertTrue(guild.available)
        self.assertEqual(guild.shard_id, 1)
        self.assertIsNone(guild.splash)
        self.assertIsNone(guild.banner)
        self.assertIsNone(guild.description)
        self.assertEqual(guild.verification_level, 2)
        self.assertIsNone(guild.vanity_url_code)
        self.assertEqual(guild.nsfw_level, 1)
        self.assertEqual(guild.premium_subscription_count, 5)
        self.assertIsNone(guild.discovery_splash)
        self.assertEqual(guild.member_count, 50)
        self.assertFalse(guild.large)
        self.assertTrue(guild.premium_progress_bar_enabled)
        self.assertIsNone(guild.application_id)
        self.assertEqual(guild.afk_timeout, 300)
        self.assertIsNone(guild.afk_channel_id)
        self.assertIsNone(guild.system_channel_id)
        self.assertEqual(guild.premium_tier, 3)
        self.assertIsNone(guild.widget_enabled)
        self.assertIsNone(guild.widget_channel_id)
        self.assertEqual(guild.explicit_content_filter, 2)
        self.assertEqual(guild.mfa_level, 1)
        self.assertEqual(guild.joined_timestamp, 1624914000)
        self.assertEqual(guild.default_message_notifications, 1)
        self.assertEqual(guild.maximum_members, 100)
        self.assertEqual(guild.max_video_channel_users, 10)
        self.assertEqual(guild.max_stage_video_channel_users, 5)
        self.assertIsNone(guild.approximate_member_count)
        self.assertIsNone(guild.approximate_presence_count)
        self.assertIsNone(guild.vanity_url_uses)
        self.assertIsNone(guild.rules_channel_id)
        self.assertIsNone(guild.public_updates_channel_id)
        self.assertEqual(guild.preferred_locale, "en-US")
        self.assertIsNone(guild.safety_alerts_channel_id)
        self.assertEqual(guild.owner_id, "456")
