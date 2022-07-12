"""GUI base class"""

class GUI:
    """Base class for all client GUI implementations"""

    def add_message(self, msg: str) -> None:
        """
        Add a message to the GUI display

        :param msg: Message to add
        """
        raise NotImplementedError()

    def conn_failed(self) -> None:
        """
        Show a connection failure
        """
        raise NotImplementedError()
