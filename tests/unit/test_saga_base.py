"""
test the saga_base module
"""
from tc_messageBroker.rabbit_mq.saga.saga_base import Saga
from tc_messageBroker.rabbit_mq.saga.choreography import ChoreographyDict
from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from datetime import datetime
from tc_messageBroker.rabbit_mq.status import Status


def test_choreagraphy_sorting_orders_predefined_choreogprahy():
    saga = Saga(
        ChoreographyDict.DISCORD_UPDATE_CHANNELS,
        Status.NOT_STARTED,
        data=None,
        created_at=datetime.now(),
    )

    ## it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 4
    order_val = 0
    for tx in tx_sorted:
        if tx.status == Status.NOT_STARTED:
            assert order_val < tx.order
            order_val = tx.order


def test_assert_sorting_status_predefined_choreagprahy():
    """assert the NOT_STARTED transactions to be at the top of the list"""

    saga = Saga(
        ChoreographyDict.DISCORD_UPDATE_CHANNELS,
        Status.NOT_STARTED,
        data=None,
        created_at=datetime.now(),
    )

    ## it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 4

    condition = False
    for tx in tx_sorted:
        if tx.status == Status.NOT_STARTED:
            assert condition is False
        else:
            condition = True


def test_choreagraphy_sorting_orders_random_choreogprahy():
    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue", "event", 2, Status.NOT_STARTED),
            ITransaction("queue", "event", 4, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    ## it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 2
    order_val = 0
    for tx in tx_sorted:
        if tx.status == Status.NOT_STARTED:
            assert order_val < tx.order
            order_val = tx.order


def test_choreagraphy_sorting_status_random_choreogprahy():
    """assert the NOT_STARTED transactions to be at the top of the list"""

    choreography = IChoreography(
        name="choreography_with_random_tx",
        transactions=[
            ITransaction("queue", "event", 5, Status.IN_PROGRESS),
            ITransaction("queue", "event", 2, Status.NOT_STARTED),
            ITransaction("queue", "event", 4, Status.NOT_STARTED),
            ITransaction("queue", "event", 3, Status.SUCCESS),
            ITransaction("queue", "event", 1, Status.FAILED),
            ITransaction("queue", "event", 0, Status.CANCELLED),
        ],
    )

    saga = Saga(choreography, Status.NOT_STARTED, data=None, created_at=datetime.now())

    ## it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 2

    condition = False
    status = []
    for tx in tx_sorted:
        status.append(tx.status)
        if tx.status == Status.NOT_STARTED:
            assert condition is False
        else:
            condition = True
