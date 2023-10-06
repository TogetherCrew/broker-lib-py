class Attachment:
    def __init__(
        self,
        id: str,
        filename: str | None = None,
        description: str | None = None,
        content_type: str | None = None,
        size: int | None = None,
        url: str | None = None,
        proxy_url: str | None = None,
        height: int | None = None,
        width: int | None = None,
        ephemeral: bool | None = False,
        duration_secs: float | None = None,
        waveform: str | None = None,
        flags: int | None = None,
    ) -> None:
        self.id = id
        self.filename = filename
        self.description = description
        self.content_type = content_type
        self.size = size
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
        self.ephemeral = ephemeral
        self.duration_secs = duration_secs
        self.waveform = waveform
        self.flags = flags

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id=d["id"],
            filename=d.get("filename"),
            description=d.get("description"),
            content_type=d.get("content_type"),
            size=d.get("size"),
            url=d.get("url"),
            proxy_url=d.get("proxy_url"),
            height=d.get("height"),
            width=d.get("width"),
            ephemeral=d.get("ephemeral", False),
            duration_secs=d.get("duration_secs"),
            waveform=d.get("waveform"),
            flags=d.get("flags"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "description": self.description,
            "content_type": self.content_type,
            "size": self.size,
            "url": self.url,
            "proxy_url": self.proxy_url,
            "height": self.height,
            "width": self.width,
            "ephemeral": self.ephemeral,
            "duration_secs": self.duration_secs,
            "waveform": self.waveform,
            "flags": self.flags,
        }
