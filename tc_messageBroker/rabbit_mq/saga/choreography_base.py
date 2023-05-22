from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction


class IChoreography:
    def __init__(self, name: str, transactions: list[ITransaction]) -> None:
        self.name = name
        self.transactions = transactions
