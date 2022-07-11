"""Work with different event types"""

import enum

class Event(enum.Enum):
    """Enumeration of all events. The ordering should not be relied on."""
    CONN_FAIL = enum.auto()
    MSG_RECV = enum.auto()
    MSG_SEND = enum.auto()
