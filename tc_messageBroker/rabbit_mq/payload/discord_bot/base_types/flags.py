class BitFields:
    def __init__(self, bitfield: int | None = None, flags: str | None = None) -> None:
        self.bitfield = bitfield
        self.flags = flags

    @classmethod
    def from_dict(cls, data: dict) -> "BitFields":
        return cls(bitfield=data.get("bitfield"), flags=data.get("flags"))

    def to_dict(self) -> dict:
        data = {"bitfield": self.bitfield, "flags": self.flags}
        return data


class PermissionsBitField:
    def __init__(
        self,
        bitfield: int | None = None,
        all_permissions: int | None = None,
        default_permissions: int | None = None,
        permission_flags: dict | None = None,
        stage_moderator: int | None = None,
    ) -> None:
        self.bitfield = bitfield
        self.all_permissions = all_permissions
        self.default_permissions = default_permissions
        self.permission_flags = permission_flags
        self.stage_moderator = stage_moderator

    @classmethod
    def from_dict(cls, d: dict) -> "PermissionsBitField":
        return cls(
            bitfield=d.get("bitfield"),
            all_permissions=d.get("allPermissions"),
            default_permissions=d.get("defaultPermissions"),
            permission_flags=d.get("permissionFlags"),
            stage_moderator=d.get("stageModerator"),
        )

    def to_dict(self) -> dict:
        return {
            "bitfield": self.bitfield,
            "allPermissions": self.all_permissions,
            "defaultPermissions": self.default_permissions,
            "permissionFlags": self.permission_flags,
            "stageModerator": self.stage_moderator,
        }
