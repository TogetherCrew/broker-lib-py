"""
testing the saga object
"""
from tc_messageBroker.rabbit_mq.saga.saga_base import get_saga
from tc_messageBroker.rabbit_mq.status import Status
from datetime import datetime
import pytest


# @pytest.mark.skip(
#     reason="Unable to test on GitHub Actions (no available MongoDB instance)"
# )
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
