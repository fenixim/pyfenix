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
        self._quit = False

        self._gui.set_cb("on_send", self._api.send_message)
        self._gui.set_cb("on_quit", self.kill)

    def run(self):
        """
        Start the loop

        Polls for messages and updates the GUI.
        """
        while not self._quit:
            self._gui.add_messages(self._api.poll_messages())

    def kill(self):
        """
        Kill the loop cleanly
        """
        self._quit = True
