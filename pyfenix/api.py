"""API base class"""

from typing import Tuple

class API:
    """Base class for all client API implementations"""

    async def connect(self, server: Tuple[str, int]) -> None:
        """
        Connect to the server
        """
        raise NotImplementedError

    def send(self, msg: str) -> None:
        """
        Send a message to the server
        """
        raise NotImplementedError

    async def recv_event(self) -> None:
        """
        Handle one event from server
        """
        raise NotImplementedError
