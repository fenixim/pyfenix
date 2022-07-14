"""Implementation of the client API layer for websockets"""

import json
import logging
import queue
from typing import Optional, Tuple

import websockets.client

from pyfenix.api import API
from pyfenix.event import Event

class WebsocketsAPI(API):
    """Fenix client API using websockets"""

    def __init__(self, event_queue: queue.Queue):
        """
        :param event_queue: Event queue shared by the event loop and GUI
        """
        self._conn: Optional[websockets.client.WebSocketClientProtocol] = None
        self._queue = event_queue
        self._server_uri: Optional[str] = None

    async def connect(self, server: Tuple[str, int]) -> None:
        """
        Establish a connection to a Fenix server

        An Event.CONN_FAIL event will be generated if the connection fails.

        :param server: (address, port) pair, for example ("127.0.0.1", 21337)
        """
        address, port = server
        self._server_uri = f"ws://{address}:{port}"

        try:
            self._conn = await websockets.client.connect(self._server_uri)
        except (ConnectionRefusedError, OSError):
            self._queue.put((Event.CONN_FAIL, ""))

    async def close(self) -> None:
        """
        Closes the connection to the Fenix server

        Safe to call more than once
        """
        if self._conn is not None:
            await self._conn.close()
            self._conn = None

    def send(self, msg: str) -> None:
        """
        Send a message to the server
        """
        raise NotImplementedError()

    async def recv_event(self) -> None:
        """
        Recv one event from the server and parse it into the queue
        """
        if self._conn is None:
            raise NoConnectionError()

        msg = json.loads(await self._conn.recv())
        if msg["type"] == "msg_send":
            if msg["message"]:
                self._queue.put((Event.MSG_RECV, "yay"))
        else:
            logging.warning("Unrecognized protocol %s", msg["type"])

class NoConnectionError(Exception):
    """Represents an attempt to use the API without a connection"""
