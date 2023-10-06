from .guild import Guild


class Member:
    def __init__(
        self,
        guild: Guild | None = None,
        joined_timestamp: int | None = None,
        premium_since_timestamp: int | None = None,
        nickname: str | None = None,
        pending: bool | None = None,
        communication_disabled_until_timestamp: int | None = None,
        avatar: str | None = None,
        flags: int | None = None,
    ):
        self.guild = guild
        self.joined_timestamp = joined_timestamp
        self.premium_since_timestamp = premium_since_timestamp
        self.nickname = nickname
        self.pending = pending
        self.communication_disabled_until_timestamp = (
            communication_disabled_until_timestamp
        )
        self.avatar = avatar
        self.flags = flags

    @classmethod
    def from_dict(cls, member_dict: dict, guild: Guild):
        """
        convert the dicrionary data into the Member class instance
        Note that the keys should follow the camelCase format

        Parameters
        ------------
        member_dict : dict
            the dictionary of member data
        guild : Guild
            the guild data instance

        Returns
        --------
        member : Member
            the class instance
        """
        return cls(
            guild=guild,
            joined_timestamp=member_dict.get("joinedTimestamp"),
            premium_since_timestamp=member_dict.get("premiumSubscriptionCount"),
            nickname=member_dict.get("nickname"),
            pending=member_dict.get("pending"),
            communication_disabled_until_timestamp=member_dict.get(
                "communicationDisabledUntilTimestamp"
            ),
            avatar=member_dict.get("avatar"),
            flags=member_dict.get("flags"),
        )

    def to_dict(self) -> dict:
        """
        convert the class data into a dictionary
        Note that the keys would follow the camelCase format

        Parameters
        -------------
        member : Member
            the member we want to convert

        Returns
        --------
        member_dict : dict
            the class data converted to dictionary
        """
        return {
            "joinedTimestamp": self.joined_timestamp,
            "premiumSubscriptionCount": self.premium_since_timestamp,
            "nickname": self.nickname,
            "pending": self.pending,
            "communicationDisabledUntilTimestamp": self.communication_disabled_until_timestamp,
            "avatar": self.avatar,
            "flags": self.flags,
        }
