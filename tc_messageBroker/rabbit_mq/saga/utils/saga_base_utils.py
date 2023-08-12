# Doing the object to dict and vice operations here
from typing import Any

from tc_messageBroker.rabbit_mq.saga.transactions import ITransaction


def get_transactions(transactions: list[dict[str, Any]]) -> list[ITransaction]:
    transactions_obj = []

    for tx in transactions:
        transaction = ITransaction(**tx)
        transactions_obj.append(transaction)

    return transactions_obj


def convert_tx_dict(transaction: ITransaction):
    """
    convert the transaction into a dictionary
    """
    tx_dict: dict[str, Any] = {}

    tx_dict["queue"] = transaction.queue
    tx_dict["event"] = transaction.event
    tx_dict["order"] = transaction.order
    tx_dict["status"] = transaction.status

    if transaction.start is not None:
        tx_dict["start"] = transaction.start
    if transaction.end is not None:
        tx_dict["end"] = transaction.end
    if transaction.message is not None:
        tx_dict["message"] = transaction.message
    if transaction.runtime is not None:
        tx_dict["runtime"] = transaction.runtime
    if transaction.error is not None:
        tx_dict["error"] = transaction.error

    return tx_dict
