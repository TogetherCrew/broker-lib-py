class TC_message_broker:
    def __init__(self, broker_url: str) -> None:
        self.broker_url = broker_url

    def __new__(cls, broker_url: str):
        ## making it singleton
        if not hasattr(cls, "instance"):
            cls.instance = super(
                TC_message_broker, 
                cls).__new__(cls)
        return cls.instance
