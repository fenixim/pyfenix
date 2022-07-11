class ClientAPIStub:

    def __init__(self):
        self._messages = []

    def get(self):
        if self._messages:
            return self._messages.pop(0)

    def set_messages(self, messages):
        self._messages = messages
