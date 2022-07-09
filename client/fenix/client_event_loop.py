"""Event handler loop for all client events."""

class ClientEventLoop:
    """Updates GUI on new events. Should not be run in main thread."""

    def __init__(self, client_api):
        """
        :param client_api: API implementation of the Fenix protocol
        """
        self._api = client_api

    def run(self):
        """
        Start the loop

        As of now this does nothing.
        """

    def kill(self):
        """
        Kill the loop cleanly

        This is intended to be used as a callback. As of now, it does nothing.
        """
