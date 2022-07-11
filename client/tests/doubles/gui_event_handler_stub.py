class GUIEventHandlerStub:

    def __init__(self):
        self._conn_failed = False
        self._messages = []

    def add_message(self, message):
        self._messages.append(message)

    def get_messages(self):
        return self._messages

    def conn_failed(self):
        self._conn_failed = True

    def is_connection_failed(self):
        return self._conn_failed
