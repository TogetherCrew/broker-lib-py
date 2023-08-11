from datetime import datetime

from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.saga_base import Saga
from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.status import Status


def test_start_tx():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.NOT_STARTED),
            ITransaction("queue1", "event1", 2, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    def sample_publish(**kwargs):
        assert kwargs["queue_name"] == choreography.transactions[1].queue
        assert kwargs["event"] == choreography.transactions[1].event
        assert kwargs["content"]["uuid"] == saga.uuid

    saga.start(
        publish_method=sample_publish,
        mongo_creds={},
        test_mode=True,
    )

    assert saga.status == Status.IN_PROGRESS
    assert saga.choreography.transactions[0].status == Status.NOT_STARTED
    assert saga.choreography.transactions[1].status == Status.NOT_STARTED
    assert saga.choreography.transactions[2].status == Status.SUCCESS
    assert saga.choreography.transactions[3].status == Status.FAILED
    assert saga.choreography.transactions[4].status == Status.CANCELLED
