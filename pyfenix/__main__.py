"""Fenix runner"""

import queue
import threading

from tests.doubles import ClientAPIStub, GUIEventHandlerStub

from .client_event_loop import ClientEventLoop

event_queue: queue.Queue = queue.Queue()
api = ClientAPIStub(event_queue)
gui = GUIEventHandlerStub(event_queue)

handler = ClientEventLoop(event_queue, api, gui)
handler_thread = threading.Thread(target=handler.run)
handler_thread.start()
