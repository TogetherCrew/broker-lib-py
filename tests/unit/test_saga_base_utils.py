from datetime import datetime, timedelta

from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction
from tc_messageBroker.rabbit_mq.saga.utils.saga_base_utils import (
    convert_tx_dict,
    get_transactions,
)


def test_convert_transaction_to_dict_keys():
    queue = "sample_queue"
    event = "sample_event"
    order = 1
    status = "SAMPLE_STATUS"
    tx = ITransaction(
        queue=queue,
        event=event,
        order=order,
        status=status,
    )

    tx_dict = convert_tx_dict(tx)

    keys = tx_dict.keys()

    assert "queue" in keys
    assert "event" in keys
    assert "order" in keys
    assert "status" in keys


def test_convert_transaction_to_dict_values():
    queue = "sample_queue"
    event = "sample_event"
    order = 1
    status = "SAMPLE_STATUS"
    tx = ITransaction(
        queue=queue,
        event=event,
        order=order,
        status=status,
    )

    tx_dict = convert_tx_dict(tx)

    assert tx_dict["queue"] == queue
    assert tx_dict["event"] == event
    assert tx_dict["order"] == order
    assert tx_dict["status"] == status


def test_convert_transaction_to_dict_additional_params():
    queue = "sample_queue"
    event = "sample_event"
    order = 1
    status = "SAMPLE_STATUS"
    start = datetime.now() - timedelta(minutes=1)
    end = datetime.now()
    runtime = (end - start).microseconds * 1000
    message = {"data"}
    error = "Error"

    tx = ITransaction(
        queue=queue,
        event=event,
        order=order,
        status=status,
        start=start,
        end=end,
        runtime=runtime,
        message=message,
        error=error,
    )

    tx_dict = convert_tx_dict(tx)

    assert tx_dict["queue"] == queue
    assert tx_dict["event"] == event
    assert tx_dict["order"] == order
    assert tx_dict["status"] == status
    assert tx_dict["start"] == start
    assert tx_dict["end"] == end
    assert tx_dict["runtime"] == runtime
    assert tx_dict["message"] == message


def test_get_transactions_length():
    event = "EVENT"
    queue = "QUEUE"
    order = 1
    status = "STATUS"

    transactions = []
    loop_iter = 2
    for i in range(loop_iter):
        tx = {}
        tx["event"] = event + str(i)
        tx["queue"] = queue + str(i)
        tx["order"] = order + i
        tx["status"] = status + str(i)

        transactions.append(tx)

    transactions_obj = get_transactions(transactions)

    assert len(transactions_obj) == loop_iter


def test_get_transactions_obj():
    event = "EVENT"
    queue = "QUEUE"
    order = 1
    status = "STATUS"

    transactions = []
    loop_iter = 2
    for i in range(loop_iter):
        tx = {}
        tx["event"] = event + str(i)
        tx["queue"] = queue + str(i)
        tx["order"] = order + i
        tx["status"] = status + str(i)

        transactions.append(tx)

    transactions_obj = get_transactions(transactions)

    for i in range(loop_iter):
        assert isinstance(transactions_obj[i], ITransaction) is True
