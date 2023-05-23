from tc_messageBroker.rabbit_mq.status import Status


def test_enum_stats():
    assert Status.NOT_STARTED == "NOT_STARTED"
    assert Status.IN_PROGRESS == "IN_PROGRESS"
    assert Status.SUCCESS == "SUCCESS"
    assert Status.FAILED == "FAILED"
    assert Status.CANCELLED == "CANCELLED"
