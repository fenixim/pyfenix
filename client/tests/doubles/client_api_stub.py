class ClientAPIStub:

    def __init__(self):
        self._messages = []

    def poll_messages(self):
        return self._messages

    def set_messages(self, messages):
        self._messages = messages
