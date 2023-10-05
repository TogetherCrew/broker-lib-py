class Embed:
    def __init__(
        self,
        title: str | None = None,
        type: str | None = None,
        description: str | None = None,
        url: str | None = None,
        timestamp: str | None = None,
        color: int | None = None,
        footer: dict | None = None,
        image: dict | None = None,
        thumbnail: dict | None = None,
        video: dict | None = None,
        provider: dict | None = None,
        author: dict | None = None,
        fields: list[dict] | None = None,
    ) -> None:
        self.title = title
        self.type = type
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.video = video
        self.provider = provider
        self.author = author
        self.fields = fields

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            title=d.get("title"),
            type=d.get("type", "rich"),
            description=d.get("description"),
            url=d.get("url"),
            timestamp=d.get("timestamp"),
            color=d.get("color"),
            footer=d.get("footer"),
            image=d.get("image"),
            thumbnail=d.get("thumbnail"),
            video=d.get("video"),
            provider=d.get("provider"),
            author=d.get("author"),
            fields=d.get("fields"),
        )

    def to_dict(self):
        return {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "footer": self.footer,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "video": self.video,
            "provider": self.provider,
            "author": self.author,
            "fields": self.fields,
        }
