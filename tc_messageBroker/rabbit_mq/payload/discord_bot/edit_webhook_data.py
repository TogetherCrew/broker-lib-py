from .base_types.allowed_mentions import AllowedMentions
from .base_types.attachment import Attachment
from .base_types.embed import Embed


class InteractionResponseEditData:
    def __init__(
        self,
        thread_id: int | None = None,
        content: str | None = None,
        embeds: list[Embed] | None = None,
        allowed_mentions: AllowedMentions | None = None,
        components: list[list[dict]] | None = None,
        files: list[dict] | None = None,
        payload_json: str | None = None,
        attachments: list[Attachment] | None = None,
    ):
        """
        to set the right values to this please refer to
        https://discord.com/developers/docs/resources/webhook#edit-webhook-message

        for `components` please refer to
        https://discord.com/developers/docs/interactions/message-components
        """
        self.thread_id = thread_id
        self.content = content
        self.embeds = embeds
        self.allowed_mentions = allowed_mentions
        self.components = components
        self.files = files
        self.payload_json = payload_json
        self.attachments = attachments

    def to_dict(self) -> dict:
        data_dict = {}
        if self.content is not None:
            data_dict["content"] = self.content
        if self.thread_id is not None:
            data_dict["thread_id"] = str(self.thread_id)
        if self.embeds is not None:
            data_dict["embeds"] = str([embed.to_dict() for embed in self.embeds])
        if self.allowed_mentions is not None:
            data_dict["allowed_mentions"] = str(self.allowed_mentions.to_dict())
        if self.components is not None:
            # data_dict["components"] = [
            #     [comp.to_dict() for comp in row] for row in self.components
            # ]
            data_dict["components"] = str(self.components)
        if self.files is not None:
            data_dict["files"] = str(self.files)
        if self.payload_json is not None:
            data_dict["payload_json"] = self.payload_json
        if self.attachments is not None:
            data_dict["attachments"] = str(
                [attachment.to_dict() for attachment in self.attachments]
            )
        return data_dict

    @classmethod
    def from_dict(cls, data_dict: dict):
        content = data_dict.get("content")
        embeds = [
            Embed.from_dict(embed_dict) for embed_dict in data_dict.get("embeds", [])
        ]
        allowed_mentions = AllowedMentions.from_dict(
            data_dict.get("allowed_mentions", {})
        )
        components = data_dict.get("components")
        files = data_dict.get("files", [])
        payload_json = data_dict.get("payload_json")
        attachments = [
            Attachment.from_dict(attachment_dict)
            for attachment_dict in data_dict.get("attachments", [])
        ]
        return cls(
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            files=files,
            payload_json=payload_json,
            attachments=attachments,
        )
