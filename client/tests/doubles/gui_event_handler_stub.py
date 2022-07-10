class GUIEventHandlerStub:

    def __init__(self):
        self._messages = []
        self._quit = False
        self._event_cb_on_send = lambda *args: None
        self._event_cb_on_quit = lambda *args: None

    def add_messages(self, messages):
        self._messages.extend(messages)
        if messages:
            self._quit = True

    def get_messages(self):
        return self._messages

    def send_message(self, msg):
        self._event_cb_on_send(msg)

    def set_cb(self, name, cb):
        setattr(self, f"_event_cb_{name}", cb)

    def quit(self):
        self._event_cb_on_quit()
