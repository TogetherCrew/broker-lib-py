from datetime import datetime


class User:
    def __init__(
        self,
        id: str,
        created_at: datetime | None = None,
        partial: bool | None = None,
        default_avatar_url: str | None = None,
        client: dict | None = None,
        created_timestamp: int | None = None,
        discriminator: str | None = None,
        bot: bool | None = None,
        avatar: str | None = None,
        avatar_decoration: str | None = None,
        banner: str | None = None,
        accent_color: int | None = None,
        display_name: str | None = None,
        dm_channel: dict | None = None,
        flags: int | None = None,
        global_name: str | None = None,
        hex_accent_color: str | None = None,
        system: bool | None = None,
        tag: str | None = None,
        username: str | None = None,
    ) -> None:
        self.id = id
        self.created_at = created_at
        self.client = client
        self.default_avatar_url = default_avatar_url
        self.partial = partial
        self.created_timestamp = created_timestamp
        self.discriminator = discriminator
        self.bot = bot
        self.avatar = avatar
        self.avatar_decoration = avatar_decoration
        self.banner = banner
        self.accent_color = accent_color
        self.display_name = display_name
        self.dm_channel = dm_channel
        self.flags = flags
        self.global_name = global_name
        self.hex_accent_color = hex_accent_color
        self.system = system
        self.tag = tag
        self.username = username

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        created_at = data.get("createdAt")
        if created_at is not None:
            created_at = datetime.fromisoformat(created_at)

        return cls(
            id=data["id"],
            created_at=created_at,
            client=data.get("client"),
            default_avatar_url=data.get("defaultAvatarURL"),
            partial=data.get("partial"),
            created_timestamp=data.get("createdTimestamp"),
            discriminator=data.get("discriminator"),
            bot=data.get("bot"),
            avatar=data.get("avatar"),
            avatar_decoration=data.get("avatarDecoration"),
            banner=data.get("banner"),
            accent_color=data.get("accentColor"),
            display_name=data.get("displayName"),
            dm_channel=data.get("dmChannel"),
            flags=data.get("flags"),
            global_name=data.get("globalName"),
            hex_accent_color=data.get("hexAccentColor"),
            system=data.get("system"),
            tag=data.get("tag"),
            username=data.get("username"),
        )

    def to_dict(self) -> dict:
        created_at = self.created_at
        if self.created_at is not None:
            created_at = self.created_at

        data = {
            "id": self.id,
            "created_at": created_at,
            "client": self.client,
            "defaultAvatarURL": self.default_avatar_url,
            "partial": self.partial,
            "createdTimestamp": self.created_timestamp,
            "discriminator": self.discriminator,
            "bot": self.bot,
            "avatar": self.avatar,
            "avatarDecoration": self.avatar_decoration,
            "banner": self.banner,
            "accentColor": self.accent_color,
            "displayName": self.display_name,
            "dmChannel": self.dm_channel,
            "flags": self.flags,
            "globalName": self.global_name,
            "hexAccentColor": self.hex_accent_color,
            "system": self.system,
            "tag": self.tag,
            "username": self.username,
        }
        return data
