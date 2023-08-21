from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.transactions import (
    DISCORD_SCHEDULED_JOB_TRANSACTIONS,
    DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)


def test_choreography_discord_update_channels_no_inputs():
    choreography = IChoreography(name=None, transactions=None)

    assert choreography.name is None
    assert choreography.transactions is None


def test_choreography_discord_update_channels():
    choreography = IChoreography(
        name="sample", transactions=DISCORD_UPDATE_CHANNELS_TRANSACTIONS
    )

    assert choreography.name == "sample"
    assert choreography.transactions == DISCORD_UPDATE_CHANNELS_TRANSACTIONS


def test_choreography_discord_update_channels_wrong_input():
    choreography = IChoreography(
        name="sample", transactions=DISCORD_UPDATE_CHANNELS_TRANSACTIONS
    )

    assert choreography.name != "some_choreography"
    assert choreography.transactions != DISCORD_SCHEDULED_JOB_TRANSACTIONS


def test_choreography_discord_job_transactions():
    choreography = IChoreography(
        name="sample", transactions=DISCORD_SCHEDULED_JOB_TRANSACTIONS
    )

    assert choreography.name == "sample"
    assert choreography.transactions == DISCORD_SCHEDULED_JOB_TRANSACTIONS
