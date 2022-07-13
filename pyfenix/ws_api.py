"""Implementation of the client API layer for websockets"""

import queue
from typing import Tuple

from pyfenix.api import API
from pyfenix.event import Event

class WebsocketsAPI(API):
    """Fenix client API using websockets"""

    def __init__(self, event_queue: queue.Queue):
        """
        :param event_queue: Event queue shared by the event loop and GUI
        """
        self._queue = event_queue

    def connect(self, server: Tuple[int, str]) -> None:
        """
        Establish a connection to a Fenix server

        The connection is automatically failed, because it isn't implemented.

        :param server: (address, port) pair, for example ("127.0.0.1", 21337)
        """
        self._queue.put((Event.CONN_FAIL, ""))
