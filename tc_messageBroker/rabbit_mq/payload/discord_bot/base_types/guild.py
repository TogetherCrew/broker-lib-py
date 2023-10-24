from typing import Any


class Guild:
    def __init__(
        self,
        id: str | None = None,
        name: str | None = None,
        icon: str | None = None,
        features: list[str] = [],
        available: bool | None = None,
        shard_id: int | None = None,
        splash: str | None = None,
        banner: str | None = None,
        channels: list[str] | None = None,
        members: list[str] | None = None,
        roles: list[str] | None = None,
        commands: Any | None = None,
        bans: Any | None = None,
        description: str | None = None,
        verification_level: int | None = None,
        vanity_url_code: str | None = None,
        nsfw_level: int | None = None,
        premium_subscription_count: int | None = None,
        discovery_splash: str | None = None,
        member_count: int | None = None,
        large: bool | None = None,
        premium_progress_bar_enabled: bool | None = None,
        application_id: str | None = None,
        afk_timeout: int | None = None,
        afk_channel_id: str | None = None,
        system_channel_id: str | None = None,
        premium_tier: int | None = None,
        widget_enabled: bool | None = None,
        widget_channel_id: str | None = None,
        explicit_content_filter: int | None = None,
        mfa_level: int | None = None,
        joined_timestamp: int | None = None,
        default_message_notifications: int | None = None,
        maximum_members: int | None = None,
        max_video_channel_users: int | None = None,
        max_stage_video_channel_users: int | None = None,
        approximate_member_count: int | None = None,
        approximate_presence_count: int | None = None,
        vanity_url_uses: int | None = None,
        rules_channel_id: str | None = None,
        public_updates_channel_id: str | None = None,
        preferred_locale: str | None = None,
        safety_alerts_channel_id: str | None = None,
        owner_id: str | None = None,
    ) -> None:
        self.id = id
        self.name = name
        self.icon = icon
        self.features = features
        self.available = available
        self.members = members
        self.channels = channels
        self.roles = roles
        self.commands = commands
        self.bans = bans
        self.shard_id = shard_id
        self.splash = splash
        self.banner = banner
        self.description = description
        self.verification_level = verification_level
        self.vanity_url_code = vanity_url_code
        self.nsfw_level = nsfw_level
        self.premium_subscription_count = premium_subscription_count
        self.discovery_splash = discovery_splash
        self.member_count = member_count
        self.large = large
        self.premium_progress_bar_enabled = premium_progress_bar_enabled
        self.application_id = application_id
        self.afk_timeout = afk_timeout
        self.afk_channel_id = afk_channel_id
        self.system_channel_id = system_channel_id
        self.premium_tier = premium_tier
        self.widget_enabled = widget_enabled
        self.widget_channel_id = widget_channel_id
        self.explicit_content_filter = explicit_content_filter
        self.mfa_level = mfa_level
        self.joined_timestamp = joined_timestamp
        self.default_message_notifications = default_message_notifications
        self.maximum_members = maximum_members
        self.max_video_channel_users = max_video_channel_users
        self.max_stage_video_channel_users = max_stage_video_channel_users
        self.approximate_member_count = approximate_member_count
        self.approximate_presence_count = approximate_presence_count
        self.vanity_url_uses = vanity_url_uses
        self.rules_channel_id = rules_channel_id
        self.public_updates_channel_id = public_updates_channel_id
        self.preferred_locale = preferred_locale
        self.safety_alerts_channel_id = safety_alerts_channel_id
        self.owner_id = owner_id

    @classmethod
    def from_dict(cls, guild_dict: dict) -> "Guild":
        """
        from the dict create the class instance
        Note that the keys of given guild should follow the camelCase format
        """
        return cls(
            id=guild_dict.get("id"),
            name=guild_dict.get("name"),
            icon=guild_dict.get("icon"),
            features=guild_dict.get("features", []),
            channels=guild_dict.get("channels"),
            members=guild_dict.get("members"),
            roles=guild_dict.get("roles"),
            commands=guild_dict.get("commands"),
            bans=guild_dict.get("bans"),
            available=guild_dict.get("available"),
            shard_id=guild_dict.get("shardId"),
            splash=guild_dict.get("splash"),
            banner=guild_dict.get("banner"),
            description=guild_dict.get("description"),
            verification_level=guild_dict.get("verificationLevel"),
            vanity_url_code=guild_dict.get("vanityURLCode"),
            nsfw_level=guild_dict.get("nsfwLevel"),
            premium_subscription_count=guild_dict.get("premiumSubscriptionCount"),
            discovery_splash=guild_dict.get("discoverySplash"),
            member_count=guild_dict.get("memberCount"),
            large=guild_dict.get("large"),
            premium_progress_bar_enabled=guild_dict.get("premiumProgressBarEnabled"),
            application_id=guild_dict.get("applicationId"),
            afk_timeout=guild_dict.get("afkTimeout"),
            afk_channel_id=guild_dict.get("afkChannelId"),
            system_channel_id=guild_dict.get("systemChannelId"),
            premium_tier=guild_dict.get("premiumTier"),
            widget_enabled=guild_dict.get("widgetEnabled"),
            widget_channel_id=guild_dict.get("widgetChannelId"),
            explicit_content_filter=guild_dict.get("explicitContentFilter"),
            mfa_level=guild_dict.get("mfaLevel"),
            joined_timestamp=guild_dict.get("joinedTimestamp"),
            default_message_notifications=guild_dict.get("defaultMessageNotifications"),
            maximum_members=guild_dict.get("maximumMembers"),
            max_video_channel_users=guild_dict.get("maxVideoChannelUsers"),
            max_stage_video_channel_users=guild_dict.get("maxStageVideoChannelUsers"),
            approximate_member_count=guild_dict.get("approximateMemberCount"),
            approximate_presence_count=guild_dict.get("approximatePresenceCount"),
            vanity_url_uses=guild_dict.get("vanityURLUses"),
            rules_channel_id=guild_dict.get("rulesChannelId"),
            public_updates_channel_id=guild_dict.get("publicUpdatesChannelId"),
            preferred_locale=guild_dict.get("preferredLocale"),
            safety_alerts_channel_id=guild_dict.get("safetyAlertsChannelId"),
            owner_id=guild_dict.get("ownerId"),
        )

    def to_dict(self) -> dict:
        """
        Convert the data into guild instance.
        Note that the kyes would follow the camelCase format

        Parameters
        -----------
        guild : Guild
            the guild object to be converted to dict

        Return
        -------
        data : dict
            the data converted to dict
        """
        data = {}

        if self.id is not None:
            data["id"] = self.id
        if self.name is not None:
            data["name"] = self.name
        if self.icon is not None:
            data["icon"] = self.icon
        if self.features is not None:
            data["features"] = self.features  # type: ignore
        if self.available is not None:
            data["available"] = self.available  # type: ignore
        if self.shard_id is not None:
            data["shardId"] = self.shard_id  # type: ignore
        if self.splash is not None:
            data["splash"] = self.splash  # type: ignore
        if self.banner is not None:
            data["banner"] = self.banner  # type: ignore
        if self.description is not None:
            data["description"] = self.description  # type: ignore
        if self.verification_level is not None:
            data["verificationLevel"] = self.verification_level  # type: ignore
        if self.vanity_url_code is not None:
            data["vanityURLCode"] = self.vanity_url_code  # type: ignore
        if self.nsfw_level is not None:
            data["nsfwLevel"] = self.nsfw_level  # type: ignore
        if self.premium_subscription_count is not None:
            data[
                "premiumSubscriptionCount"
            ] = self.premium_subscription_count  # type: ignore
        if self.discovery_splash is not None:
            data["discoverySplash"] = self.discovery_splash  # type: ignore
        if self.member_count is not None:
            data["memberCount"] = self.member_count  # type: ignore
        if self.large is not None:
            data["large"] = self.large  # type: ignore
        if self.premium_progress_bar_enabled is not None:
            data[
                "premiumProgressBarEnabled"
            ] = self.premium_progress_bar_enabled  # type: ignore
        if self.application_id is not None:
            data["applicationId"] = self.application_id  # type: ignore
        if self.afk_timeout is not None:
            data["afkTimeout"] = self.afk_timeout  # type: ignore
        if self.afk_channel_id is not None:
            data["afkChannelId"] = self.afk_channel_id  # type: ignore
        if self.system_channel_id is not None:
            data["systemChannelId"] = self.system_channel_id  # type: ignore
        if self.premium_tier is not None:
            data["premiumTier"] = self.premium_tier  # type: ignore
        if self.widget_enabled is not None:
            data["widgetEnabled"] = self.widget_enabled  # type: ignore
        if self.widget_channel_id is not None:
            data["widgetChannelId"] = self.widget_channel_id  # type: ignore
        if self.explicit_content_filter is not None:
            data["explicitContentFilter"] = self.explicit_content_filter  # type: ignore
        if self.mfa_level is not None:
            data["mfaLevel"] = self.mfa_level  # type: ignore
        if self.joined_timestamp is not None:
            data["joinedTimestamp"] = self.joined_timestamp  # type: ignore
        if self.default_message_notifications is not None:
            data[
                "defaultMessageNotifications"
            ] = self.default_message_notifications  # type: ignore
        if self.maximum_members is not None:
            data["maximumMembers"] = self.maximum_members  # type: ignore
        if self.max_video_channel_users is not None:
            data["maxVideoChannelUsers"] = self.max_video_channel_users  # type: ignore
        if self.max_stage_video_channel_users is not None:
            data[
                "maxStageVideoChannelUsers"
            ] = self.max_stage_video_channel_users  # type: ignore
        if self.approximate_member_count is not None:
            data["approximateMemberCount"] = self.approximate_member_count  # type: ignore
        if self.approximate_presence_count is not None:
            data["approximatePresenceCount"] = self.approximate_presence_count  # type: ignore
        if self.vanity_url_uses is not None:
            data["vanityURLUses"] = self.vanity_url_uses  # type: ignore
        if self.rules_channel_id is not None:
            data["rulesChannelId"] = self.rules_channel_id
        if self.public_updates_channel_id is not None:
            data["publicUpdatesChannelId"] = self.public_updates_channel_id
        if self.preferred_locale is not None:
            data["preferredLocale"] = self.preferred_locale
        if self.safety_alerts_channel_id is not None:
            data["safetyAlertsChannelId"] = self.safety_alerts_channel_id
        if self.owner_id is not None:
            data["ownerId"] = self.owner_id
        if self.channels is not None:
            data["channels"] = self.channels  # type: ignore
        if self.members is not None:
            data["members"] = self.members  # type: ignore
        if self.roles is not None:
            data["roles"] = self.roles  # type: ignore
        if self.commands is not None:
            data["commands"] = self.commands
        if self.bans is not None:
            data["bans"] = self.bans

        return data
