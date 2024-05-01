# vim: set shiftwidth=2 tabstop=2 softtabstop=2 expandtab:

from pynput import keyboard
from pynput.keyboard import Key, Controller

kb=keyboard.Controller()

def darwin_intercept(event_type, event):
    if (event_type!=10):
      return event
    import Quartz
    global cmd
    length, chars = Quartz.CGEventKeyboardGetUnicodeString(
        event, 100, None, None)
    if length > 0 and chars == 'v':
        kb.press("7")
        kb.release("7")
        return None
    else:
        return event

with keyboard.Listener(
        darwin_intercept=darwin_intercept) as listener:
    listener.join()
