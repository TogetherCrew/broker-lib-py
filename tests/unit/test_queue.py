from tc_messageBroker.rabbit_mq.queue import Queue


def test_queue():
    assert Queue.SERVER_API == "SERVER_API"
    assert Queue.DISCORD_ANALYZER == "DISCORD_ANALYZER"
    assert Queue.DISCORD_BOT == "DISCORD_BOT"
    assert Queue.TWITTER_ANALYZER == "TWITTER_ANALYZER"
    assert Queue.TWITTER_BOT == "TWITTER_BOT"
    assert Queue.HIVEMIND == "HIVEMIND"
