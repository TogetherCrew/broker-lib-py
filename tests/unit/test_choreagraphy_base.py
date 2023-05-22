from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.transactions import (
    DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)


def test_choreography():
    choreography = IChoreography(
        name="sample", transactions=DISCORD_UPDATE_CHANNELS_TRANSACTIONS
    )

    assert choreography.name == "sample"
    assert choreography.transactions == DISCORD_UPDATE_CHANNELS_TRANSACTIONS
