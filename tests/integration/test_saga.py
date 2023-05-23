"""
testing the saga object
"""
from tc_messageBroker.rabbit_mq.saga.saga_base import get_saga, Saga
from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from datetime import datetime
from tc_messageBroker.rabbit_mq.saga.transactions import (
    DISCORD_UPDATE_CHANNELS_TRANSACTIONS,
)
from tc_messageBroker.rabbit_mq.status import Status
import numpy as np
from copy import deepcopy
import pytest


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no available MongoDB instance)"
)
def test_inputs():
    connection_url = "mongodb://127.0.0.1:27017/"

    ## we should have this data before running this test in db
    saga = get_saga(guildId="993163081939165234", connection_url=connection_url)

    assert saga.choreography is not None
    assert saga.status in [
        Status.IN_PROGRESS,
        Status.CANCELLED,
        Status.FAILED,
        Status.NOT_STARTED,
        Status.SUCCESS,
    ]
    assert isinstance(saga.created_at, datetime) is True
    assert isinstance(saga.uuid, str) is True


@pytest.mark.skip(
    reason="Unable to test on GitHub Actions (no available MongoDB instance)"
)
def test_saga_update():
    """
    test updating a saga instance in db
    """
    connection_url = "mongodb://127.0.0.1:27017/"

    choreography = IChoreography(
        name="sample", transactions=deepcopy(DISCORD_UPDATE_CHANNELS_TRANSACTIONS)
    )

    saga = Saga(
        choreography=choreography,
        status=Status.NOT_STARTED,
        data={"guildId": "1234"},
        created_at=datetime.now(),
    )

    tx = np.array(choreography.transactions)
    tx[0].status = Status.SUCCESS

    saga._update_save(transactions=tx, mongo_connection=connection_url)
