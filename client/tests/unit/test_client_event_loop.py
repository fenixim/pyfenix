import threading
import time

import pytest

from fenix import ClientEventLoop
from tests.doubles import ClientAPIStub
from tests.doubles import GUIEventHandlerStub

@pytest.fixture
def api():
    return ClientAPIStub()

@pytest.fixture
def gui():
    return GUIEventHandlerStub()

@pytest.fixture
def handler(api, gui):
    return ClientEventLoop(api, gui)

def test_given_no_new_messages_when_poll_will_not_change_gui(gui, handler):
    handler.handle_next_event()
    assert not gui.get_messages()

def test_given_two_messages_when_poll_will_show_first(api, gui, handler):
    api.set_messages(["yay", "yeet"])
    handler.handle_next_event()
    assert gui.get_messages() == ["yay"]

def test_given_two_messages_when_poll_twice_will_show_two(api, gui, handler):
    api.set_messages(["yay", "yeet"])
    handler.handle_next_event()
    handler.handle_next_event()
    assert gui.get_messages() == ["yay", "yeet"]
