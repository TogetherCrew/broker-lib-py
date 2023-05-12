from tc_messageBroker.rabbit_mq.utils.event import Event
from tc_messageBroker.rabbit_mq.utils.event import Status
from datetime import datetime, timedelta


def test_event_default():
    event_name = "name"
    event_description = "description"
    event_message = "message"
    event_status = Status.FAILED
    event_start = datetime.timestamp(datetime.now() - timedelta(days=1))
    event_end = datetime.timestamp(datetime.now())
    event_runtime = 10000
    event_error = ValueError

    event_obj = Event(
        name=event_name,
        description=event_description,
        status=event_status,
        start=event_start,
        end=event_end,
        runtime=event_runtime,
        error=event_error,
        message=event_message,
    )

    assert event_obj.name == event_name
    assert event_obj.description == event_description
    assert event_obj.status == event_status
    assert event_obj.start == event_start
    assert event_obj.end == event_end
    assert event_obj.runtime == event_runtime
    assert event_obj.error == event_error
    assert event_obj.message == event_message


def test_event_empty_inputs():
    event_name = ""
    event_description = ""
    event_message = ""
    event_status = Status.SUCCESS
    # event_start = datetime.timestamp(datetime.now() - timedelta(days=1))
    event_start = datetime(1970, 1, 1).timestamp()
    event_end = datetime.now().timestamp()
    event_runtime = 0
    event_error = None

    event_obj = Event(
        name=event_name,
        description=event_description,
        status=event_status,
        start=event_start,
        end=event_end,
        runtime=event_runtime,
        error=event_error,
        message=event_message,
    )

    assert event_obj.name == event_name
    assert event_obj.description == event_description
    assert event_obj.status == event_status
    assert event_obj.start == event_start
    assert event_obj.end == event_end
    assert event_obj.runtime == event_runtime
    assert event_obj.error == event_error
    assert event_obj.message == event_message

