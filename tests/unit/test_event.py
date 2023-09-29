from tc_messageBroker.rabbit_mq.event import Event


def test_enum_event_default():
    # For now we have the events below
    assert Event.SERVER_API.UPDATE_GUILD == "UPDATE_GUILD"
    assert Event.DISCORD_BOT.FETCH == "FETCH"
    assert Event.DISCORD_BOT.SEND_MESSAGE == "SEND_MESSAGE"
    assert Event.DISCORD_ANALYZER.RUN == "RUN"
    assert Event.DISCORD_ANALYZER.RUN_ONCE == "RUN_ONCE"
    assert Event.DISCORD_BOT.FETCH_MEMBERS == "FETCH_MEMBERS"
    assert Event.TWITTER_ANALYZER.RUN == "RUN"
    assert Event.TWITTER_BOT.EXTRACT.PROFILES == "EXTRACT_PROFILES"
    assert Event.TWITTER_BOT.EXTRACT.LIKES == "EXTRACT_LIKES"
    assert Event.TWITTER_BOT.EXTRACT.TWEETS == "EXTRACT_TWEETS"
    assert Event.TWITTER_BOT.SEND_MESSAGE == "SEND_MESSAGE"
    assert Event.HIVEMIND.INTERACTION_CREATED == "INTERACTION_CREATED"
    assert Event.HIVEMIND.QUEUE_MESSAGES_UPDATED == "QUEUE_MESSAGES_UPDATED"
    # assert Event.DISCORD_ANALYZER.SAVE == "SAVE"
