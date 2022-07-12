"""API base class"""

class API:
    """Base class for all client API implementations"""

    def send(self, msg: str) -> None:
        """
        Send a message to the server
        """
        raise NotImplementedError
