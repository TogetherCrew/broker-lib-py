from .base_types.allowed_mentions import AllowedMentions
from .base_types.attachment import Attachment
from .base_types.embed import Embed


class FollowUpMessageData:
    def __init__(
        self,
        content: str | None = None,
        username: str | None = None,
        avatar_url: str | None = None,
        tts: bool | None = None,
        embeds: list[Embed] | None = None,
        allowed_mentions: AllowedMentions | None = None,
        components: list[dict] | None = None,
        files: list[dict] | None = None,
        payload_json: str | None = None,
        attachments: list[Attachment] | None = None,
        flags: int | None = None,
        thread_name: str | None = None,
    ):
        """
        to set the right values to this please refer to
        https://discord.com/developers/docs/resources/webhook#execute-webhook

        for `component` please refer to
        https://discord.com/developers/docs/interactions/message-components
        """
        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.tts = tts
        self.embeds = embeds
        self.allowed_mentions = allowed_mentions
        self.components = components
        self.files = files
        self.payload_json = payload_json
        self.attachments = attachments
        self.flags = flags
        self.thread_name = thread_name

    def to_dict(self) -> dict:
        data = {}
        if self.content is not None:
            data["content"] = self.content
        if self.username is not None:
            data["username"] = self.username
        if self.avatar_url is not None:
            data["avatar_url"] = self.avatar_url
        if self.tts is not None:
            data["tts"] = self.tts  # type: ignore
        if self.embeds is not None:
            data["embeds"] = [embed.to_dict() for embed in self.embeds]  # type: ignore
        if self.allowed_mentions is not None:
            data["allowed_mentions"] = str(self.allowed_mentions.to_dict())
        if self.components is not None:
            # data["components"] = [component.to_dict() for component in self.components]
            data["components"] = self.components  # type: ignore
        if self.files is not None:
            data["files"] = self.files  # type: ignore
        if self.payload_json is not None:
            data["payload_json"] = self.payload_json
        if self.attachments is not None:
            data["attachments"] = [
                attachment.to_dict() for attachment in self.attachments
            ]  # type: ignore
        if self.flags is not None:
            data["flags"] = self.flags  # type: ignore
        if self.thread_name is not None:
            data["thread_name"] = self.thread_name
        return data

    @classmethod
    def from_dict(cls, data: dict):
        content = data.get("content")
        username = data.get("username")
        avatar_url = data.get("avatar_url")
        tts = data.get("tts")
        embeds = data.get("embeds")
        allowed_mentions = data.get("allowed_mentions")
        files = data.get("files")
        payload_json = data.get("payload_json")
        attachments = data.get("attachments")
        flags = data.get("flags")
        thread_name = data.get("thread_name")

        if embeds is not None:
            embeds = [Embed.from_dict(embed_dict) for embed_dict in embeds]

        if allowed_mentions is not None:
            allowed_mentions = AllowedMentions.from_dict(allowed_mentions)
        components = data.get("components")

        if attachments is not None:
            attachments = [
                Attachment.from_dict(attachment_dict) for attachment_dict in attachments
            ]

        return cls(
            content=content,
            username=username,
            avatar_url=avatar_url,
            tts=tts,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            files=files,
            payload_json=payload_json,
            attachments=attachments,
            flags=flags,
            thread_name=thread_name,
        )
