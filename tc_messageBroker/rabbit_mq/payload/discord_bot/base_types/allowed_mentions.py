class AllowedMentions:
    def __init__(
        self,
        parse: list[str] | None = None,
        roles: list[int] | None = None,
        users: list[str] | None = None,
        replied_user: bool | None = None,
    ) -> None:
        self.parse = parse
        self.roles = roles
        self.users = users
        self.replied_user = replied_user

    @classmethod
    def from_dict(cls, d: dict) -> "AllowedMentions":
        return cls(
            parse=d.get(["parse"]),
            roles=d.get(["roles"]),
            users=d.get(["users"]),
            replied_user=d.get(["replied_user"]),
        )

    def to_dict(self) -> dict:
        return {
            "parse": self.parse,
            "roles": self.roles,
            "users": self.users,
            "replied_user": self.replied_user,
        }
