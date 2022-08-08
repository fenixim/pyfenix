"""Runs the GUI interface."""

__all__ = ("TkGUI",)

from queue import Queue

from tkinter.scrolledtext import ScrolledText
from tkinter import Text, Tk
from tkinter import ttk

from .event import Event
from .gui import GUI

_EMPTY_DISPLAY_ROW = 1
_MAX_DISPLAY_ROWS = 40

class TkGUI(GUI):
    """Defines the GUI methods."""

    def __init__(self, event_queue: Queue) -> None:
        """Initialize the GUI."""
        self._event_queue = event_queue

        self._root = Tk()
        self._frm = ttk.Frame(self._root)
        self._frm.grid()

        ttk.Button(self._frm, text="Quit", command=self._quit, width=60).grid(
            column=0, row=0)

        self._display_window = ScrolledText(self._frm, width=80, height=20)
        self._display_window.grid(column=0, row=1)
        self._display_window["state"] = "disabled"

        self._input_window = Text(self._frm, width=82, height=4)
        self._input_window.grid(column=0, row=2)

        ttk.Button(self._frm, text="Send", command=self.send_message).grid(
            column=1, row=2)

    def run(self) -> None:
        """Start the GUI."""
        self._root.mainloop()
        self._display_window.insert("end -1 chars", "GUI mainloop started.")

    def add_message(self, msg: str) -> None:
        """Print a message in the display window"""
        self._display_window["state"] = "normal"

        last_row_number, _ = self._display_window.index("end").split(".")
        if int(last_row_number) > _MAX_DISPLAY_ROWS + _EMPTY_DISPLAY_ROW:
            self._display_window.delete(1.0, 2.0)
        self._display_window.insert("end -1 chars", msg + "\n")
        self._display_window["state"] = "disabled"

    def send_message(self) -> None:
        """Send the current message and clear the input window."""
        self._event_queue.put((Event.MSG_SEND, self._input_window.get("1.0", "end")))
        self._input_window.delete("1.0", "end")

    def conn_failed(self) -> None:
        """Inform the user of a connection failure."""
        print("Connection failure")
        self.add_message("Failed to connect to server.")

    def _quit(self) -> None:
        """All systems failed, get out now."""
        self._event_queue.put((Event.QUIT, None))
        self._root.destroy()
