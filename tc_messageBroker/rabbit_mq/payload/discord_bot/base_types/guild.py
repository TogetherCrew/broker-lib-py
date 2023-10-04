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

    def to_dict(self, guild) -> dict:
        """
        Convert the data into guild instance.
        Note that the kyes would follow the camelCase format

        Parameters
        -----------
        guild : Guild
            the guild object to be converted to dict

        Return
        -------
        guild_dict : dict
            the data converted to dict
        """
        return {
            "id": guild.id,
            "name": guild.name,
            "icon": guild.icon,
            "features": guild.features,
            "available": guild.available,
            "shardId": guild.shard_id,
            "splash": guild.splash,
            "banner": guild.banner,
            "description": guild.description,
            "verificationLevel": guild.verification_level,
            "vanityURLCode": guild.vanity_url_code,
            "nsfwLevel": guild.nsfw_level,
            "premiumSubscriptionCount": guild.premium_subscription_count,
            "discoverySplash": guild.discovery_splash,
            "memberCount": guild.member_count,
            "large": guild.large,
            "premiumProgressBarEnabled": guild.premium_progress_bar_enabled,
            "applicationId": guild.application_id,
            "afkTimeout": guild.afk_timeout,
            "afkChannelId": guild.afk_channel_id,
            "systemChannelId": guild.system_channel_id,
            "premiumTier": guild.premium_tier,
            "widgetEnabled": guild.widget_enabled,
            "widgetChannelId": guild.widget_channel_id,
            "explicitContentFilter": guild.explicit_content_filter,
            "mfaLevel": guild.mfa_level,
            "joinedTimestamp": guild.joined_timestamp,
            "defaultMessageNotifications": guild.default_message_notifications,
            "maximumMembers": guild.maximum_members,
            "maxVideoChannelUsers": guild.max_video_channel_users,
            "maxStageVideoChannelUsers": guild.max_stage_video_channel_users,
            "approximateMemberCount": guild.approximate_member_count,
            "approximatePresenceCount": guild.approximate_presence_count,
            "vanityURLUses": guild.vanity_url_uses,
            "rulesChannelId": guild.rules_channel_id,
            "publicUpdatesChannelId": guild.public_updates_channel_id,
            "preferredLocale": guild.preferred_locale,
            "safetyAlertsChannelId": guild.safety_alerts_channel_id,
            "ownerId": guild.owner_id,
        }
