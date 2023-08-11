"""
test the saga_base module
"""
from datetime import datetime

from tc_messageBroker.rabbit_mq.saga.choreography import ChoreographyDict
from tc_messageBroker.rabbit_mq.saga.choreography_base import IChoreography
from tc_messageBroker.rabbit_mq.saga.saga_base import Saga
from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.status import Status


def test_choreagraphy_sorting_orders_predefined_choreogprahy():
    saga = Saga(
        ChoreographyDict.DISCORD_UPDATE_CHANNELS,
        Status.NOT_STARTED,
        data=None,
        created_at=datetime.now(),
    )

    # it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 3
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

    # it should sort the NOT_STARTED transactions
    (tx_sorted, not_started_count) = saga._sort_transactions(
        saga.choreography.transactions
    )

    assert not_started_count == 3

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

    # it should sort the NOT_STARTED transactions
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

    # it should sort the NOT_STARTED transactions
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


def test_saga_create_data():
    saga_data = {"guild": "some_guildId"}
    creation_date = datetime.now()

    saga = Saga(
        ChoreographyDict.DISCORD_UPDATE_CHANNELS,
        Status.NOT_STARTED,
        data=saga_data,
        created_at=creation_date,
    )

    saga_dict = saga._create_data()

    assert (
        saga_dict["choreography"]["name"]
        == ChoreographyDict.DISCORD_UPDATE_CHANNELS.name
    )

    # we had a list of transactions
    for idx, tx in enumerate(saga_dict["choreography"]["transactions"]):
        predefined_tx = ChoreographyDict.DISCORD_UPDATE_CHANNELS.transactions[idx]
        assert tx["queue"] == predefined_tx.queue
        assert tx["event"] == predefined_tx.event
        assert tx["order"] == predefined_tx.order
        assert tx["status"] == predefined_tx.status
        # these should be not defined in predefine transaction
        assert "start" not in tx.keys()
        assert "end" not in tx.keys()
        assert "runtime" not in tx.keys()
        assert "message" not in tx.keys()
        assert "error" not in tx.keys()

        assert predefined_tx.start is None
        assert predefined_tx.end is None
        assert predefined_tx.message is None
        assert predefined_tx.runtime is None
        assert predefined_tx.error is None

    assert saga_dict["status"] == Status.NOT_STARTED
    assert saga_dict["data"] == saga_data
    assert saga_dict["sagaId"] == saga.uuid
    assert saga_dict["createdAt"] == creation_date
    assert saga_dict["updatedAt"] is not None
