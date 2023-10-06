from .attachment import Attachment
from .embed import Embed


class InteractionCallbackData:
    def __init__(
        self,
        tts: bool | None = None,
        content: str | None = None,
        embeds: list[Embed] | None = None,
        allowed_mentions: str | None = None,
        flags: int | None = None,
        components: list[dict] | None = None,
        attachments: list[Attachment] | None = None,
    ) -> None:
        """
        to set the right values please refer to
        https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure

        for `components` please refer to
        https://discord.com/developers/docs/interactions/message-components
        """
        self.tts = tts
        self.content = content
        self.embeds = embeds
        self.allowed_mentions = allowed_mentions
        self.flags = flags
        self.components = components
        self.attachments = attachments

    @classmethod
    def from_dict(cls, d: dict) -> "InteractionCallbackData":
        embeds = d.get("embeds")
        if embeds is not None:
            embeds = [Embed.from_dict(embed) for embed in embeds]

        attachments = d.get("attachments")
        if attachments is not None:
            attachments = [
                Attachment.from_dict(attachment) for attachment in attachments
            ]

        component = d.get("components")
        return cls(
            tts=d.get("tts"),
            content=d.get("content"),
            embeds=embeds,
            allowed_mentions=d.get("allowed_mentions"),
            flags=d.get("flags"),
            components=component,
            attachments=attachments,
        )

    def to_dict(self):
        embeds = None
        if self.embeds is not None:
            embeds = [embed.to_dict() for embed in self.embeds]

        components = self.components

        attachments = None
        if self.attachments:
            attachments = [attachment.to_dict() for attachment in self.attachments]

        return {
            "tts": self.tts,
            "content": self.content,
            "embeds": embeds,
            "allowed_mentions": self.allowed_mentions,
            "flags": self.flags,
            "components": components,
            "attachments": attachments,
        }
