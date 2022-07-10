class ClientAPIStub:

    def __init__(self):
        self._messages = []
        self._sent = None

    def poll_messages(self):
        messages = self._messages
        if messages:
            self._messages = []
        return messages

    def send_message(self, msg):
        self._sent = msg        

    def set_messages(self, messages):
        self._messages = messages

    def get_sent(self):
        return self._sent
