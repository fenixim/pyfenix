"""Fenix runner"""

import asyncio
from queue import Queue
import threading

from tests.doubles import GUIEventHandlerStub

from .client_event_loop import ClientEventLoop
from .ws_api import WebsocketsAPI

async def main() -> None:
    """Run Fenix"""
    event_queue: Queue = Queue()
    api = WebsocketsAPI(event_queue)
    await api.connect(("localhost", 60221))
    await api.send("yay")
    asyncio.create_task(api.listen())

    gui = GUIEventHandlerStub(event_queue)

    handler = ClientEventLoop(event_queue, api, gui)
    handler_thread = threading.Thread(target=handler.run)
    handler_thread.start()

    await api.close()

asyncio.get_event_loop().run_until_complete(main())
