import threading

from fenix import ClientEventLoop
from tests.doubles import ClientAPIStub
from tests.doubles import GUIEventHandlerStub

def test_given_no_new_messages_when_poll_then_gui_will_not_change():
    gui = GUIEventHandlerStub()
    handler = ClientEventLoop(ClientAPIStub(), gui)
    handler_thread = threading.Thread(target=handler.run, daemon=True)

    handler_thread.start()
    handler_thread.join(0.2)
    assert not gui.get_messages()

def test_given_one_new_message_when_poll_then_gui_will_have_that_message():
    gui = GUIEventHandlerStub()
    api = ClientAPIStub()
    handler = ClientEventLoop(api, gui)
    handler_thread = threading.Thread(target=handler.run, daemon=True)

    handler_thread.start()
    api.set_messages(["yay", "yeet"])
    handler_thread.join(0.2)

    assert not handler_thread.is_alive()
    assert gui.get_messages() == ["yay", "yeet"]
