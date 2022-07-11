"""Event handler loop for all client events."""

class ClientEventLoop:
    """Updates GUI on new events. Should not be run in main thread."""

    def __init__(self, client_api, client_gui):
        """
        :param client_api: API implementation of the Fenix protocol
        :param client_gui: GUI implementation
        """
        self._api = client_api
        self._gui = client_gui

    def run(self):
        """
        Start the loop

        Polls for messages and updates the GUI.
        """
        while True:
            self.handle_next_event()

    def handle_next_event(self):
        """
        Handle one event off the queue
        """
        event = self._api.get()
        if event:
            self._gui.add_message(event)
