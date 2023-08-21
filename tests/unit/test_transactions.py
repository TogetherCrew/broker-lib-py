from datetime import datetime, timedelta

from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.status import Status


def test_transaction_default():
    transaction = ITransaction(
        queue=Queue.DISCORD_ANALYZER,
        event=Event.DISCORD_ANALYZER.RUN,
        order=1,
        status=Status.NOT_STARTED,
    )

    assert transaction.queue == Queue.DISCORD_ANALYZER
    assert transaction.event == Event.DISCORD_ANALYZER.RUN
    assert transaction.order == 1
    assert transaction.status == Status.NOT_STARTED
    assert transaction.message is None
    assert transaction.start is None
    assert transaction.end is None
    assert transaction.runtime is None
    assert transaction.error is None


def test_transaction_all_inputs():
    """
    transaction with all inputs given
    """
    now = datetime.now()

    transaction = ITransaction(
        queue=Queue.DISCORD_ANALYZER,
        event=Event.DISCORD_ANALYZER.RUN,
        order=1,
        status=Status.NOT_STARTED,
        message="sample_message",
        start=now - timedelta(minutes=5),
        end=now,
        runtime=10000,
        error=None,
    )

    assert transaction.queue == Queue.DISCORD_ANALYZER
    assert transaction.event == Event.DISCORD_ANALYZER.RUN
    assert transaction.order == 1
    assert transaction.status == Status.NOT_STARTED
    assert transaction.message == "sample_message"
    assert transaction.start == now - timedelta(minutes=5)
    assert transaction.end == now
    assert transaction.runtime == 10000
    assert transaction.error is None
