"""Work with different event types"""

import enum

class Event(enum.Enum):
    """
    Enumeration of all events. The ordering should not be relied on.

    CONN_FAIL indicates a failure to connect to the Fenix server
    MSG_RECV indicates an incoming message event
    MSG_SEND indicates an outgoing message event
    QUIT should be used to terminate all threads cleanly
    """
    CONN_FAIL = enum.auto()
    MSG_RECV = enum.auto()
    MSG_SEND = enum.auto()
    QUIT = enum.auto()
