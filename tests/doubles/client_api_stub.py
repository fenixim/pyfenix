import queue

from pyfenix import API
from pyfenix import Event

class ClientAPIStub(API):

    def __init__(self, queue: queue.Queue):
        self._sent = None
        self._queue = queue

    def set_messages(self, messages):
        for msg in messages:
            self._queue.put((Event.MSG_RECV, msg))

    def fail_connect(self):
        self._queue.put((Event.CONN_FAIL, None))

    async def send(self, msg):
        self._sent = msg

    def get_sent(self):
        return self._sent

class NoConnectionError(Exception):
    pass
