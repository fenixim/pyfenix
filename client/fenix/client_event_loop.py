"""Event handler loop for all client events."""

from fenix.event import Event

class ClientEventLoop:
    """Updates GUI on new events. Should not be run in main thread."""

    def __init__(self, event_queue, client_api, client_gui):
        """
        :param client_api: API implementation of the Fenix protocol
        :param client_gui: GUI implementation
        """
        self._api = client_api
        self._gui = client_gui
        self._queue = event_queue

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
        if self._queue.empty():
            return

        event = self._queue.get_nowait()
        event_type, payload = event

        if event_type == Event.CONN_FAIL:
            self._gui.conn_failed()
        elif event_type == Event.MSG_SEND:
            self._api.send(payload)
        else:
            self._gui.add_message(payload)
