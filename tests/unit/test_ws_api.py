import queue

from pyfenix import WebsocketsAPI, Event

def test_when_server_is_not_running_will_add_failed_connection_event():
    event_queue = queue.Queue()
    api = WebsocketsAPI(event_queue)
    api.connect(("127.0.0.1", 21337))
    assert event_queue.get_nowait() == (Event.CONN_FAIL, "")
