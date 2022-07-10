import threading
import time

import pytest

from fenix import ClientEventLoop
from tests.doubles import ClientAPIStub
from tests.doubles import GUIEventHandlerStub

@pytest.fixture
def gui():
    return GUIEventHandlerStub()

@pytest.fixture
def api():
    return ClientAPIStub()

@pytest.fixture(autouse=True)
def handler_thread(gui, api):
    handler = ClientEventLoop(api, gui)
    thread = threading.Thread(target=handler.run, daemon=True)
    thread.start()

def test_given_no_new_messages_when_poll_then_gui_will_not_change(gui):
    assert not gui.get_messages()

def test_given_one_new_message_when_poll_then_gui_will_show_it(gui, api):
    api.set_messages(["yay", "yeet"])
    time.sleep(0.2)
    assert gui.get_messages() == ["yay", "yeet"]

def test_given_gui_when_gui_sends_message_then_loop_will_send_to_api(gui, api):
    gui.send_message("yay")
    assert api.get_sent() == "yay"
