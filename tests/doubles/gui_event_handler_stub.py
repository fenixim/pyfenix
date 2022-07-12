from pyfenix import Event

class GUIEventHandlerStub:

    def __init__(self, queue):
        self._conn_failed = False
        self._messages = []
        self._queue = queue

    def add_message(self, message):
        self._messages.append(message)

    def get_messages(self):
        return self._messages

    def conn_failed(self):
        self._conn_failed = True

    def is_connection_failed(self):
        return self._conn_failed

    def set_send(self, msg):
        self._queue.put((Event.MSG_SEND, msg))

    def quit(self):
        self._queue.put((Event.QUIT, None))
