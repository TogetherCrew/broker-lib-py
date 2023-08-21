from .choreography_base import IChoreography
from .transactions import (DISCORD_FETCH_MEMBERS_TRANSACTIONS,
                           DISCORD_SCHEDULED_JOB_TRANSACTIONS,
                           DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
                           TWITTER_REFRESH_TRANSACTIONS)

DISCORD_UPDATE_CHANNELS = IChoreography(
    name="DISCORD_UPDATE_CHANNELS",
    transactions=DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)

DISCORD_SCHEDULED_JOB = IChoreography(
    name="DISCORD_SCHEDULED_JOB",
    transactions=DISCORD_SCHEDULED_JOB_TRANSACTIONS,
)

DISCORD_FETCH_MEMBERS = IChoreography(
    name="DISCORD_FETCH_MEMBERS",
    transactions=DISCORD_FETCH_MEMBERS_TRANSACTIONS,
)


TWITTER_REFRESH = IChoreography(
    name="TWITTER_REFRESH", transactions=TWITTER_REFRESH_TRANSACTIONS
)


class ChoreographyDict:
    DISCORD_UPDATE_CHANNELS = DISCORD_UPDATE_CHANNELS
    DISCORD_SCHEDULED_JOB = DISCORD_SCHEDULED_JOB
    DISCORD_FETCH_MEMBERS = DISCORD_FETCH_MEMBERS
    TWITTER_REFRESH = TWITTER_REFRESH
