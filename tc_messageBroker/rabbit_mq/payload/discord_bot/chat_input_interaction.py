from datetime import datetime

from .base_types.guild import Guild
from .base_types.flags import PermissionsBitField
from .base_types.user import User


class ChatInputCommandInteraction:
    def __init__(
        self,
        id: str,
        application_id: int | None = None,
        type: int | None = None,
        channel: dict | None = None,
        channel_id: str | None = None,
        token: str | None = None,
        guild_id: str | None = None,
        user: User | None = None,
        created_at: datetime | None = None,
        deffered: bool | None = None,
        replied: bool | None = None,
        webhook: dict | None = None,
        member: dict | None = None,
        ephemeral: bool | None = None,
        guild: Guild | None = None,
        created_time_stamp: int | None = None,
        app_permissions: str | None = None,
        locale: str | None = None,
        guild_locale: str | None = None,
        client: dict | None = None,
        command: dict | None = None,
        command_id: str | None = None,
        command_name: str | None = None,
        command_type: dict | None = None,
        command_guild_id: dict | None = None,
        member_permissions: PermissionsBitField | None = None,
        options: dict | None = None,
        version: int | None = None,
    ) -> None:
        """
        to set the values right please refer to
        https://old.discordjs.dev/#/docs/discord.js/14.13.0/class/ChatInputCommandInteraction
        """
        self.id = id
        self.application_id = application_id
        self.app_permissions = app_permissions
        self.channel = channel
        self.channel_id = channel_id
        self.client = client
        self.command = command
        self.command_guild_id = command_guild_id
        self.command_id = command_id
        self.command_name = command_name
        self.command_type = command_type
        self.created_at = created_at
        self.created_time_stamp = created_time_stamp
        self.deferred = deffered
        self.ephemeral = ephemeral
        self.guild = guild
        self.guild_id = guild_id
        self.guild_locale = guild_locale
        self.locale = locale
        self.member = member
        self.member_permissions = member_permissions
        self.options = options
        self.replied = replied
        self.token = token
        self.type = type
        self.user = user
        self.version = version
        self.webhook = webhook

    @classmethod
    def from_dict(self, data: dict) -> "ChatInputCommandInteraction":
        member_permissions = data.get("memberPermissions")
        if member_permissions is not None:
            member_permissions = PermissionsBitField.from_dict(member_permissions)

        created_at = data.get("createdAt")
        if created_at is not None:
            created_at = datetime.fromisoformat(created_at)

        guild = data.get("guild")
        if guild is not None:
            guild = Guild.from_dict(data.get("guild"))

        user = data.get("user")
        if user is not None:
            user = User.from_dict(user)

        return ChatInputCommandInteraction(
            id=data["id"],
            application_id=data.get("applicationId"),
            type=data.get("type"),
            channel=data.get("channel"),
            channel_id=data.get("channelId"),
            token=data.get("token"),
            guild_id=data.get("guildId"),
            user=user,
            created_at=created_at,
            deffered=data.get("deferred"),
            replied=data.get("replied"),
            webhook=data.get("webhook"),
            member=data.get("member"),
            ephemeral=data.get("ephemeral"),
            guild=guild,
            created_time_stamp=data.get("createdTimestamp"),
            app_permissions=data.get("appPermissions"),
            locale=data.get("locale"),
            guild_locale=data.get("guildLocale"),
            client=data.get("client"),
            command=data.get("command"),
            command_id=data.get("commandId"),
            command_name=data.get("commandName"),
            command_type=data.get("commandType"),
            command_guild_id=data.get("commandGuildId"),
            member_permissions=member_permissions,
            options=data.get("options"),
            version=data.get("version"),
        )

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "applicationId": self.application_id,
            "type": self.type,
            "channel": self.channel,
            "channelId": self.channel_id,
            "token": self.token,
            "guildId": self.guild_id,
            "user": self.user.to_dict(),
            "createdAt": self.created_at.isoformat(),
            "deferred": self.deferred,
            "replied": self.replied,
            "webhook": self.webhook,
        }
        if self.member:
            data["member"] = self.member
        if self.ephemeral is not None:
            data["ephemeral"] = self.ephemeral
        if self.guild:
            data["guild"] = self.guild.to_dict()
        if self.created_time_stamp is not None:
            data["created_time_stamp"] = self.created_time_stamp
        if self.app_permissions is not None:
            data["app_permissions"] = self.app_permissions
        if self.locale is not None:
            data["locale"] = self.locale
        if self.guild_locale is not None:
            data["guild_locale"] = self.guild_locale
        if self.client is not None:
            data["client"] = self.client
        if self.command is not None:
            data["command"] = self.command
        if self.command_id is not None:
            data["command_id"] = self.command_id
        if self.command_name is not None:
            data["command_name"] = self.command_name
        if self.command_type is not None:
            data["command_type"] = self.command_type
        if self.command_guild_id is not None:
            data["command_guild_id"] = self.command_guild_id
        if self.member_permissions is not None:
            data["member_permissions"] = self.member_permissions
        if self.options is not None:
            data["options"] = self.options
        if self.version is not None:
            data["version"] = self.version
        return data
