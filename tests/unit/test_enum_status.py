from tc_messageBroker.rabbit_mq.status import Status


def test_enum_stats():
    assert Status.PENDING.value == 0
    assert Status.IN_PROGRESS.value == 1
    assert Status.SUCCESS.value == 2
    assert Status.FAILED.value == 3
