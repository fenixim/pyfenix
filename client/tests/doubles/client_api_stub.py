from fenix import Event

class ClientAPIStub:

    def __init__(self):
        self._queue = []

    def get(self):
        if self._queue:
            return self._queue.pop(0)

    def set_messages(self, messages):
        for msg in messages:
            self._queue.append((Event.MSG, msg))

    def fail_connect(self):
        self._queue.append((Event.CONN_FAIL, None))

class NoConnectionError(Exception):
    pass
