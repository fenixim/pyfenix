"""Event handler loop for all client events."""

from fenix.event import Event

class ClientEventLoop:
    """Updates GUI on new events. Should not be run in main thread."""

    def __init__(self, event_queue, client_api, client_gui):
        """
        :param event_queue: Event queue shared by the API and GUI layers
        :param client_api: API implementation of the Fenix protocol
        :param client_gui: GUI implementation
        """
        self._api = client_api
        self._gui = client_gui
        self._queue = event_queue
        self._done = False

    def run(self):
        """
        Start the loop

        Polls for messages and updates the GUI.
        """
        while not self._done:
            self.handle_next_event()

    def handle_next_event(self):
        """
        Handle one event off the queue
        """
        if self._queue.empty():
            return

        event = self._queue.get_nowait()
        event_type, payload = event

        if event_type == Event.CONN_FAIL:
            self._gui.conn_failed()
        elif event_type == Event.MSG_SEND:
            self._api.send(payload)
        elif event_type == Event.QUIT:
            self._done = True
        else:
            self._gui.add_message(payload)
