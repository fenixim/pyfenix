import asyncio
import queue
import threading

import pytest

from pyfenix import ClientEventLoop
from tests.doubles import ClientAPIStub
from tests.doubles import GUIEventHandlerStub

@pytest.fixture
def event_queue():
    return queue.Queue()

@pytest.fixture
def api(event_queue):
    return ClientAPIStub(event_queue)

@pytest.fixture
def gui(event_queue):
    return GUIEventHandlerStub(event_queue)

@pytest.fixture
def handler(event_queue, api, gui):
    return ClientEventLoop(event_queue, api, gui, asyncio.get_event_loop())

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

async def test_when_send_message_will_send_through_api(api, gui, handler):
    gui.set_send("yay")
    handler.handle_next_event()
    await asyncio.sleep(0.1)
    assert api.get_sent() == "yay"

def test_when_fail_to_connect_will_show_connection_error(api, gui, handler):
    api.fail_connect()
    handler.handle_next_event()
    assert gui.is_connection_failed()

def test_quit_event_is_timely(gui, handler):
    runner = threading.Thread(target=handler.run, daemon=True)
    runner.start()
    gui.quit()
    runner.join(0.1)
    assert not runner.is_alive()
