"""Runs the GUI interface."""

from queue import Queue

from tkinter import Tk
from tkinter import ttk

from .event import Event
from .gui import GUI

class TkGUI(GUI):
    """Defines the GUI methods."""

    def __init__(self, event_queue: Queue) -> None:
        """Initialize the GUI."""
        self._event_queue = event_queue

        self._root = Tk()
        self._frm = ttk.Frame(self._root)
        self._frm.grid()
        ttk.Button(self._frm, text="Quit", command=self._quit).grid(column=1, row=0)
        self._next_msg_row = 0

    def run(self) -> None:
        """Start the GUI."""
        self._root.mainloop()

    def add_message(self, msg: str) -> None:
        """Print a message in a label."""
        ttk.Label(self._frm, text=msg).grid(column=0, row=self._next_msg_row)
        self._next_msg_row += 1

    def conn_failed(self) -> None:
        """Hope for the best."""

    def _quit(self) -> None:
        """All systems failed, get out now."""
        self._event_queue.put((Event.QUIT, None))
        self._root.destroy()
