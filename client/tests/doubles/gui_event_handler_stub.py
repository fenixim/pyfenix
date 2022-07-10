class GUIEventHandlerStub:

    def __init__(self):
        self._messages = []
        self._quit = False

    def has_quit(self):
        return self._quit

    def add_messages(self, messages):
        self._messages.extend(messages)
        if messages:
            self._quit = True

    def get_messages(self):
        return self._messages
