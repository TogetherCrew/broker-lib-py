from .choreography_base import IChoreography
from .transactions import DISCORD_UPDATE_CHANNELS_TRANSACTIONS


DISCORD_UPDATE_CHANNELS = IChoreography(
    name="DISCORD_UPDATE_CHANNELS",
    transactions=DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)


class ChoreographyDict:
    DISCORD_UPDATE_CHANNELS = DISCORD_UPDATE_CHANNELS
