import queue

import pytest
import websockets

from pyfenix import WebsocketsAPI, Event

@pytest.fixture
def event_queue():
    return queue.Queue()

@pytest.fixture
def api(event_queue):
    return WebsocketsAPI(event_queue)

@pytest.fixture
def server_fac(unused_tcp_port):
    def make_server(impl):
        return (
                   websockets.serve(impl, "127.0.0.1", unused_tcp_port),
                   unused_tcp_port
               )
    return make_server

async def test_when_server_is_not_running_will_fail_connect(unused_tcp_port):
    event_queue = queue.Queue()
    api = WebsocketsAPI(event_queue)
    await api.connect(("localhost", unused_tcp_port))
    assert event_queue.get_nowait() == (Event.CONN_FAIL, "")

async def test_when_recv_will_queue_event(api, event_queue, server_fac):
    async def send_yay(conn):
        await conn.send('{"type": "msg_send", "message": "yay"}')

    server, port = server_fac(send_yay)
    async with server:
        await api.connect(("localhost", port))
        await api.recv_event()

    assert event_queue.get_nowait() == (Event.MSG_RECV, "yay")

async def test_when_recv_empty_message_will_ignore(api, event_queue, server_fac):
    async def send_nothing(conn):
        await conn.send('{"type": "msg_send", "message": ""}')

    server, port = server_fac(send_nothing)
    async with server:
        await api.connect(("localhost", port))
        await api.recv_event()

    assert event_queue.empty()
