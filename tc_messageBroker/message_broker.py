import pika

# from typing import Callable
import logging
from datetime import datetime
import json
import functools


class RabbitMQ:
    def __init__(self, broker_url: str, port: int, username: str, password: str):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

        self.broker_url = broker_url
        self.port = port
        self._username = username
        self._password = password

        ## it will use the default exchange point if not created
        self.exchange_name = ""
        self.channel = None
        self.connection = None
        self.event_function = {}

    def __new__(cls, broker_url: str, port: int, username: str, password: str):
        ## making it singleton
        if not hasattr(cls, "instance"):
            cls.instance = super(RabbitMQ, cls).__new__(cls)
        return cls.instance

    def connect(
            self, 
            queue_name: str, 
            consume_options: dict = None,
            heartbeat: int = 60
        ) -> bool:
        """
        connect the rabbitMQ broker and start consuming

        Parameters:
        -------------
        queue_name : str
            the queue name to connect
        consume_options : dict
            additional arguments for basic_consume method
            default is `None`
        heartbeat : int
            the number of seconds for a message to stay alive
            default is 60 seconds

        Returns:
        ---------
        is_successful : bool
            if True, connecting to rabbitMQ server was successful
            otherwise would return False
        """
        try:
            credentials = pika.PlainCredentials(self._username, self._password)
            amqpServer = self.broker_url
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=amqpServer,
                    port=self.port,
                    credentials=credentials,
                    heartbeat=heartbeat, ## disabling the heartbeat
                ),
            )
            self.channel = self.connection.channel()

            # make sure that the channel is created,
            # if not this statement will create it
            self.channel.queue_declare(queue=queue_name)

            self.channel.basic_consume(
                queue=queue_name,
                on_message_callback=self._consume_callback,
                auto_ack=False,
                arguments=consume_options,
            )
            return True
        except Exception as exp:
            logging.error(f" Something went wrong with RabbitMQ {exp}")
            return False

    def _consume_callback(self, ch, method, properties, body) -> bool:
        """
        consume a message with a specific body

        Parameters:
        -------------
        method : any
            the method which have the property of delivery_tag
        body : dict[str, any]
            the dictionary containing the body of message to be consumed

        Returns:
        ---------
        is_successful : bool
            if True, the event function was called
            otherwise would return False and requeue the message
        """
        body_serialized = json.loads(body)
        event = body_serialized["event"]

        if event not in self.event_function.keys():
            logging.info(" An Event was received that doesn't exist")
            self.connection.add_callback_threadsafe(
                functools.partial(
                    self.channel.basic_reject,
                    delivery_tag=method.delivery_tag,
                    requeue=True,
                )
            )
        else:
            self.event_function[event](body_serialized)
            self.connection.add_callback_threadsafe(
                functools.partial(
                    self.channel.basic_ack,
                    delivery_tag=method.delivery_tag,
                )
            )

    def consume(self, queue_name: str, consume_options: dict = None):
        """
        set consuming events from a queue
        """
        self.channel.queue_declare(queue=queue_name)

        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=self._consume_callback,
            arguments=consume_options,
            auto_ack=False,
        )

    def publish(
        self, queue_name: str, event: str, content: dict, options: any = None
    ) -> None:
        """
        Publish a specific message to a specific queue directly

        Parameters:
        -------------
        queue_name : str
            the exchange point name
        event : str
            the event name to use
            using the events available under Event class is recommended
        content : dict
            dictionary of contents to publish
        options : any
            additional arguments for basic_publish method
            default is `None`

        """
        data = self._define_data(event=event, content=content)

        self.channel.queue_declare(queue=queue_name)

        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=queue_name,
            body=data,
            properties=options,
        )

    def on_event(self, event_name: str, on_message: callable) -> None:
        """
        set a function to be called when an event happened

        Parameters:
        -------------
        event_name : str
            the event name we're setting the function for
        on_message : callable
            the message when recieved (consumed) to call the function

        """
        self.event_function[event_name] = on_message

    def create_exchange(
        self,
        name: str,
        type: str,
        **kwargs,
    ) -> None:
        """
        create an exchange point with a specific type

        Parameters:
        -------------
        name : str
            the name of the exchange point
        type : str
            the type of exchange point
            Must be either one of the
                'direct', 'topic', 'headers', or 'fanout'
        **kwargs : dict
            durable : bool
                survive the exchange point if the server restarts
                if True, will be survvived
                if False won't be re-created after server restart
                default is True
            auto_delete : bool
                whether to delete the exchange point when no queue is bound to it
                if True, will delete the exchange point when no queue is bound to it
                else, will do otherwise
            options : any
                more options for the exchange_declare
        """
        ## default values
        durable = True
        auto_delete = False
        options = None

        if "durable" in kwargs.keys():
            durable = kwargs["durable"]
        if "auto_delete" in kwargs.keys():
            auto_delete = kwargs["auto_delete"]
        if "options" in kwargs.keys():
            options = kwargs["options"]

        self.channel.exchange_declare(
            exchange=name,
            exchange_type=type,
            durable=durable,
            auto_delete=auto_delete,
            arguments=options,
        )
        self.exchange_name = name

    def bind_queue_to_exchange(
        self, queue_name: str, exchange_name: str, pattern: str
    ) -> None:
        """
        bind a queue to a special exchange point

        Parameters:
        -----------
        queue_name : str
            the name of the queue we want to bind
        exchange_name : str
            the exchange point name
        pattern : str
            routing_key of the queue
        """
        self.channel.queue_declare(queue=queue_name)

        self.channel.queue_bind(
            queue=queue_name, exchange=exchange_name, routing_key=pattern
        )

    def publish_on_exchange(
        self,
        exchange_name: str,
        routing_key: str,
        event: str,
        content: dict,
        options=None,
    ) -> None:
        """
        Publish a specific message to an exchange point using a routing key

        Parameters:
        -------------
        exchange_name : str
            the exchange point name
        routing_key : str
            the routing key used to route the messages to one or more queues
        event : str
            the event name to use
            using the events available under Event class is recommended
        content : dict
            dictionary of contents to publish
        options : any
            the properties of basic_publish method

        """

        data = self._define_data(event=event, content=content)

        self.channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=data,
            properties=options,
        )

    def _define_data(self, event: str, content: dict) -> str:
        """
        define seriazable data to use

        Parameters:
        ------------
        event : str
            the event name to use
            using the events available under Event class is recommended
        content : dict
            dictionary of contents to publish

        Retuns:
        ---------
        data_json : str
            the data in json format wrapped into a string
        """
        data = {"event": event, "date": str(datetime.now()), "content": content}

        data_json = json.dumps(data)
        return data_json
