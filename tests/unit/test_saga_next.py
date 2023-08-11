from datetime import datetime

from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.saga_base import Saga
from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.status import Status


def test_next_single_not_started_tx():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue1", "event1", 2, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    def sample_publish(**kwargs):
        # shouldn't get to this since there isn't more than on transactions to do
        assert True is False

    def sample_call():
        calculations = 6
        return calculations

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    saga.next(
        publish_method=sample_publish,
        call_function=sample_call,
        mongo_creds={},
        test_mode=True,
    )

    assert saga.status == Status.SUCCESS
    assert saga.choreography.transactions[1].status == Status.SUCCESS


def test_next_multiple_not_started_tx():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue1", "event1", 2, Status.NOT_STARTED),
            ITransaction("queue2", "event3", 4, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    def sample_publish(**kwargs):
        assert kwargs["queue_name"] == "queue2"
        assert kwargs["event"] == "event3"
        assert kwargs["content"]["uuid"] == saga.uuid
        assert kwargs["content"]["data"] == 6

    def sample_call():
        calculations = 6
        return calculations

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    saga.next(
        publish_method=sample_publish,
        call_function=sample_call,
        mongo_creds={},
        test_mode=True,
    )

    assert saga.status == Status.IN_PROGRESS
    assert saga.choreography.transactions[1].status == Status.SUCCESS


def test_saga_fails():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue1", "event1", 2, Status.NOT_STARTED),
            ITransaction("queue1", "event1", 4, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    def sample_publish(**kwargs):
        # shouldn't get to this since there isn't more than on transactions to do
        raise ValueError("An error in pipeline!")

    def sample_call():
        calculations = 6
        return calculations

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    saga.next(
        publish_method=sample_publish,
        call_function=sample_call,
        mongo_creds={},
        test_mode=True,
    )

    assert saga.status == Status.FAILED
    assert saga.choreography.transactions[1].status == Status.SUCCESS


def test_saga_and_transaction_fails():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue1", "event1", 2, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    def sample_publish(**kwargs):
        # shouldn't get to this since there isn't more than on transactions to do
        assert True is False

    def sample_call():
        calculations = 6
        raise ValueError("An error in pipeline!")
        return calculations

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    saga.next(
        publish_method=sample_publish,
        call_function=sample_call,
        mongo_creds={},
        test_mode=True,
    )

    assert saga.status == Status.FAILED
    assert saga.choreography.transactions[1].status == Status.FAILED
