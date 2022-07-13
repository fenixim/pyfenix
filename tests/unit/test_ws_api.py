import asyncio
import queue

import websockets

from pyfenix import WebsocketsAPI, Event

async def test_when_server_is_not_running_will_fail_connect(unused_tcp_port):
    event_queue = queue.Queue()
    api = WebsocketsAPI(event_queue)
    await api.connect(("localhost", unused_tcp_port))
    assert event_queue.get_nowait() == (Event.CONN_FAIL, "")

async def test_given_connection_when_recv_will_queue_event(unused_tcp_port):

    event_queue = queue.Queue()
    api = WebsocketsAPI(event_queue)
    async def send_yay(ws):
        await ws.send("{'type': 'msg_send', 'message': 'yay'}")
    serv_fut = asyncio.Future()
    async def serve():
        async with websockets.serve(send_yay, "127.0.0.1", unused_tcp_port):
            await serv_fut
    serv = asyncio.create_task(serve())

    await api.connect(("localhost", unused_tcp_port)) 
    await api.recv_event()
    serv_fut.set_result(None)
    await serv

    assert event_queue.get_nowait() == (Event.MSG_RECV, "yay")

