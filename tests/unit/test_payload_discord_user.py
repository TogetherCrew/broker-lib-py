from datetime import datetime

from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.flags import BitFields
from tc_messageBroker.rabbit_mq.payload.discord_bot.base_types.user import User


def test_user_empty_fields_input():
    user = User(id="123")

    assert user.id == "123"
    assert user.created_at is None
    assert user.default_avatar_url is None
    assert user.partial is None
    assert user.accent_color is None
    assert user.avatar is None
    assert user.avatar_decoration is None
    assert user.banner is None
    assert user.bot is None
    assert user.client is None
    assert user.discriminator is None
    assert user.display_name is None
    assert user.dm_channel is None
    assert user.flags is None
    assert user.hex_accent_color is None
    assert user.system is None
    assert user.username is None
    assert user.tag is None


def test_user_partial_fields_input():
    time = datetime.now()
    user = User(
        id="1111", created_at=time, partial=False, default_avatar_url="sample_uri"
    )

    assert user.id == "1111"
    assert user.created_at == time
    assert user.default_avatar_url == "sample_uri"
    assert user.partial is False
    assert user.accent_color is None
    assert user.avatar is None
    assert user.avatar_decoration is None
    assert user.banner is None
    assert user.bot is None
    assert user.client is None
    assert user.discriminator is None
    assert user.display_name is None
    assert user.dm_channel is None
    assert user.flags is None
    assert user.hex_accent_color is None
    assert user.system is None
    assert user.username is None
    assert user.tag is None


def test_user_all_fields():
    time = datetime.now()

    bitfields = BitFields(0, "flag1")
    user = User(
        id="1111",
        created_at=time,
        partial=False,
        default_avatar_url="sample_uri",
        accent_color=1,
        avatar="some_avatar",
        avatar_decoration="avatar_decoration",
        display_name="some_name",
        dm_channel={"channel": "general"},
        flags=bitfields,
        global_name="global name",
        hex_accent_color="#FFBF00",
        system=False,
        tag="simple_tags",
        username="username",
        banner="some_banner",
        bot=True,
        client={"id": "223", "data": "sample_data"},
        discriminator="0",
    )

    assert user.id == "1111"
    assert user.created_at == time
    assert user.default_avatar_url == "sample_uri"
    assert user.partial is False
    assert user.accent_color == 1
    assert user.avatar == "some_avatar"
    assert user.avatar_decoration == "avatar_decoration"
    assert user.banner == "some_banner"
    assert user.bot is True
    assert user.client == {"id": "223", "data": "sample_data"}
    assert user.discriminator == "0"
    assert user.display_name == "some_name"
    assert user.dm_channel == {"channel": "general"}
    assert user.flags == bitfields
    assert user.hex_accent_color == "#FFBF00"
    assert user.system is False
    assert user.username == "username"
    assert user.tag == "simple_tags"
