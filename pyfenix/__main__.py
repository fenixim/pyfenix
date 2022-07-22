"""Fenix client runner"""

import asyncio
from queue import Queue
import threading

from .api import API
from .client_event_loop import ClientEventLoop
from .tk_gui import TkGUI
from .ws_api import WebsocketsAPI

async def start_api(api: API) -> None:
    """Connect to API and start listener."""
    fut: asyncio.Future = asyncio.Future()
    await api.connect(("localhost", 60221))
    asyncio.create_task(api.listen(fut))
    await fut

def spawn_api_thread(api: API) -> asyncio.AbstractEventLoop:
    """Start an asyncio loop in another thread to run the API."""
    loop = asyncio.get_event_loop()
    api_thread = threading.Thread(target=loop.run_until_complete, args=(start_api(api),))
    api_thread.start()

    return loop

def main() -> None:
    """Start Fenix client"""
    event_queue: Queue = Queue()
    api = WebsocketsAPI(event_queue)
    loop = spawn_api_thread(api)

    gui = TkGUI(event_queue)

    handler = ClientEventLoop(event_queue, api, gui)
    handler_thread = threading.Thread(target=handler.run)
    handler_thread.start()

    gui.run()
    asyncio.run_coroutine_threadsafe(api.close(), loop)

main()
