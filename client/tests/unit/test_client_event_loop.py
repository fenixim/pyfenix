import threading

from fenix import ClientEventLoop
from tests.doubles import GRPCClientAPIStub
from tests.doubles import GUIEventHandlerStub

def test_given_no_new_messages_when_poll_then_gui_will_not_change():
    gui = GUIEventHandlerStub()
    handler = ClientEventLoop(GRPCClientAPIStub())
    handler_thread = threading.Thread(target=handler.run)
    gui.after_message = handler.kill

    handler_thread.start()
    handler_thread.join()
    assert not gui.messages
