# tc-messageBrokerPython

[![Maintainability](https://api.codeclimate.com/v1/badges/fb4c44e3858c76cab905/maintainability)](https://codeclimate.com/github/RnDAO/tc-messageBrokerPython/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fb4c44e3858c76cab905/test_coverage)](https://codeclimate.com/github/RnDAO/tc-messageBrokerPython/test_coverage)

RabbitMQ library written in Python. Responsible for brokering messages between different services.

## Installation
To install the library first clone the code and then follow the instruction below
- `pip install .`
- `pip install -r requirements.txt`

## Usage
In your project, you could use this library by importing `tc_messageBroker` and to load sub-modules just separate it by dot. For example
- `from tc_messageBroker import RabbitMQ`
- `from tc_messageBroker.rabbit_mq.queue import Queue`
- `from tc_messageBroker.rabbit_mq.event import Event`

You can find examples under [example](example) directory.
