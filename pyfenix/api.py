"""API base class."""

from typing import Tuple

class API:
    """Base class for all client API implementations."""

    async def connect(self, server: Tuple[str, int]) -> None:
        """
        Connect to a server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    async def listen(self) -> None:
        """
        Listen for events.
        """
        while True:
            await self.recv_event()

    async def send(self, msg: str) -> None:
        """
        Send a message to the server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    async def recv_event(self) -> None:
        """
        Handle one event from server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError


class NoConnectionError(Exception):
    """Represents an attempt to use the API without a connection"""
