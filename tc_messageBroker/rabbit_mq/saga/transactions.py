from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue
from tc_messageBroker.rabbit_mq.status import Status

from .transaction_base import ITransaction

DISCORD_UPDATE_CHANNELS_TRANSACTIONS = [
    ITransaction(
        Queue.DISCORD_BOT,
        Event.DISCORD_BOT.FETCH,
        order=1,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.DISCORD_ANALYZER,
        Event.DISCORD_ANALYZER.RUN,
        order=2,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.DISCORD_BOT,
        Event.DISCORD_BOT.SEND_MESSAGE,
        order=3,
        status=Status.NOT_STARTED,
    ),
    # ITransaction(
    #     Queue.DISCORD_ANALYZER,
    #     Event.DISCORD_ANALYZER.SAVE,
    #     order=3,
    #     status=Status.NOT_STARTED,
    # ),
    # ITransaction(
    #     Queue.SERVER_API,
    #     Event.SERVER_API.UPDATE_GUILD,
    #     order=3,
    #     status=Status.NOT_STARTED,
    # ),
]

DISCORD_SCHEDULED_JOB_TRANSACTIONS = [
    # ITransaction(
    #     Queue.DISCORD_BOT,
    #     Event.DISCORD_BOT.FETCH,
    #     order=1,
    #     status=Status.NOT_STARTED,
    # ),
    ITransaction(
        Queue.DISCORD_ANALYZER,
        Event.DISCORD_ANALYZER.RUN_ONCE,
        order=1,
        status=Status.NOT_STARTED,
    ),
]

DISCORD_FETCH_MEMBERS_TRANSACTIONS = [
    ITransaction(
        Queue.DISCORD_BOT,
        Event.DISCORD_BOT.FETCH_MEMBERS,
        order=1,
        status=Status.NOT_STARTED,
    )
]

TWITTER_REFRESH_TRANSACTIONS = [
    ITransaction(
        Queue.TWITTER_BOT,
        Event.TWITTER_BOT.EXTRACT.TWEETS,
        order=1,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.TWITTER_BOT,
        Event.TWITTER_BOT.EXTRACT.LIKES,
        order=2,
        status=Status.NOT_STARTED,
    ),
    ITransaction(
        Queue.TWITTER_BOT,
        Event.TWITTER_BOT.EXTRACT.PROFILES,
        order=3,
        status=Status.NOT_STARTED,
    ),
    # ITransaction(
    #     Queue.TWITTER_ANALYZER,
    #     Event.TWITTER_ANALYZER.RUN,
    #     order=4,
    #     status=Status.NOT_STARTED,
    # ),
    ITransaction(
        Queue.DISCORD_BOT,
        Event.DISCORD_BOT.SEND_MESSAGE,
        order=4,
        status=Status.NOT_STARTED,
    ),
]
