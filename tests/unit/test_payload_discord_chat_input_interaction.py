from datetime import datetime

from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.guild import Guild
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.user import User
from tc_messageBroker.rabbit_mq.payload.discord_bot.chat_input_interaction import (
    ChatInputCommandInteraction,
)
from tc_messageBroker.rabbit_mq.payload.discord_bot.type import InteractionType


def test_team_member_empty_inputs():
    ch_interaction = ChatInputCommandInteraction(id="123")

    assert ch_interaction.id == "123"
    assert ch_interaction.application_id is None
    assert ch_interaction.type is None
    assert ch_interaction.channel is None
    assert ch_interaction.channel_id is None
    assert ch_interaction.token is None
    assert ch_interaction.guild is None
    assert ch_interaction.guild_id is None
    assert ch_interaction.user is None
    assert ch_interaction.created_at is None
    assert ch_interaction.deferred is None
    assert ch_interaction.replied is None
    assert ch_interaction.webhook is None
    assert ch_interaction.member is None
    assert ch_interaction.ephemeral is None
    assert ch_interaction.created_time_stamp is None
    assert ch_interaction.app_permissions is None
    assert ch_interaction.locale is None
    assert ch_interaction.guild_locale is None
    assert ch_interaction.client is None
    assert ch_interaction.command is None
    assert ch_interaction.command_name is None
    assert ch_interaction.command_type is None
    assert ch_interaction.command_guild_id is None
    assert ch_interaction.member_permissions is None
    assert ch_interaction.options is None
    assert ch_interaction.version is None


def test_team_member_partial_inputs():
    """
    don't change the part of optional None values
    """
    time = datetime.now()

    type = InteractionType.APPLICATION_COMMAND
    user = User(
        id="1111", created_at=time, partial=False, default_avatar_url="sample_uri"
    )

    ch_interaction = ChatInputCommandInteraction(
        id="1112",
        application_id=123,
        type=type,
        channel={"general": "213"},
        channel_id="213",
        token="sample_token1asdA",
        guild_id="12323887",
        user=user,
        created_at=time,
        deffered=True,
        replied=False,
        webhook={"id": "12399"},
    )

    assert ch_interaction.id == "1112"
    assert ch_interaction.application_id == 123
    assert ch_interaction.type == type
    assert ch_interaction.channel == {"general": "213"}
    assert ch_interaction.channel_id == "213"
    assert ch_interaction.token == "sample_token1asdA"
    assert ch_interaction.guild is None
    assert ch_interaction.guild_id == "12323887"
    assert ch_interaction.user == user
    assert ch_interaction.created_at == time
    assert ch_interaction.deferred is True
    assert ch_interaction.replied is False
    assert ch_interaction.webhook == {"id": "12399"}
    assert ch_interaction.member is None
    assert ch_interaction.ephemeral is None
    assert ch_interaction.created_time_stamp is None
    assert ch_interaction.app_permissions is None
    assert ch_interaction.locale is None
    assert ch_interaction.guild_locale is None
    assert ch_interaction.client is None
    assert ch_interaction.command is None
    assert ch_interaction.command_name is None
    assert ch_interaction.command_type is None
    assert ch_interaction.command_guild_id is None
    assert ch_interaction.member_permissions is None
    assert ch_interaction.options is None
    assert ch_interaction.version is None


def test_team_member_all_inputs_filled():
    """
    filling all values
    """
    time = datetime.now()

    type = InteractionType.APPLICATION_COMMAND
    user = User(
        id="1111", created_at=time, partial=False, default_avatar_url="sample_uri"
    )

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

    ch_interaction = ChatInputCommandInteraction(
        id="1112",
        application_id=123,
        type=type,
        channel={"general": "213"},
        channel_id="213",
        token="sample_token1asdA",
        guild=guild,
        guild_id="12323887",
        user=user,
        created_at=time,
        deffered=True,
        replied=False,
        webhook={"id": "12399023"},
        member={"sample": "membersample"},
        ephemeral=True,
        created_time_stamp=time.timestamp(),
        app_permissions="permission #1",
        locale="En",
        guild_locale="en",
        client={"sampleClient": "erfa"},
        command={"ping": "pong"},
        command_name={"ping_name": "pong_name"},
        command_type={"command_type": "type"},
        command_guild_id={"AI guys": "1232"},
        member_permissions={"permission": "101"},
        options={"sample": {"one": "1"}},
        version=1,
    )

    assert ch_interaction.id == "1112"
    assert ch_interaction.application_id == 123
    assert ch_interaction.type == type
    assert ch_interaction.channel == {"general": "213"}
    assert ch_interaction.channel_id == "213"
    assert ch_interaction.token == "sample_token1asdA"
    assert ch_interaction.guild == guild
    assert ch_interaction.guild_id == "12323887"
    assert ch_interaction.user == user
    assert ch_interaction.created_at == time
    assert ch_interaction.deferred is True
    assert ch_interaction.replied is False
    assert ch_interaction.webhook == {"id": "12399023"}
    assert ch_interaction.member == {"sample": "membersample"}
    assert ch_interaction.ephemeral is True
    assert ch_interaction.created_time_stamp == time.timestamp()
    assert ch_interaction.app_permissions == "permission #1"
    assert ch_interaction.locale == "En"
    assert ch_interaction.guild_locale == "en"
    assert ch_interaction.client == {"sampleClient": "erfa"}
    assert ch_interaction.command == {"ping": "pong"}
    assert ch_interaction.command_name == {"ping_name": "pong_name"}
    assert ch_interaction.command_type == {"command_type": "type"}
    assert ch_interaction.command_guild_id == {"AI guys": "1232"}
    assert ch_interaction.member_permissions == {"permission": "101"}
    assert ch_interaction.options == {"sample": {"one": "1"}}
    assert ch_interaction.version == 1
