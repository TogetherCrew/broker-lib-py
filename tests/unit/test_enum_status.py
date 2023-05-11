from tc_messageBroker.rabbit_mq.status import Status

def test_enum_stats():

    assert Status.PENDING == 0
    assert Status.IN_PROGRESS == 1
    assert Status.SUCCESS == 2
    assert Status.FAILED == 3
