from .choreography_base import IChoreography
from .transactions import DISCORD_UPDATE_CHANNELS_TRANSACTIONS


class DISCORD_UPDATE_CHANNELS(IChoreography):
    def __init__(self) -> None:
        super().__init__(
            name="DISCORD_UPDATE_CHANNELS",
            transaction=DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
        )


class ChoreographyDict:
    DISCORD_UPDATE_CHANNELS = DISCORD_UPDATE_CHANNELS
