from tc_messageBroker.rabbit_mq.saga.transaction_base import ITransaction


class IChoreography:
    def __init__(self, name: str, transaction: ITransaction) -> None:
        self.name = name
        self.transaction = transaction


# class IChoreographyDict:
#     def __init__(self, choreography_dict: dict[str, IChoreography]) -> None:
#         self.choreography_dict = choreography_dict
