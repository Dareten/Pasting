import keyboard
import win32clipboard
from time import sleep

def foo():
    sleep(1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData().replace('\n', '').replace('\t', '')
    win32clipboard.CloseClipboard()
    keyboard.write(data, delay=0.01)
    keyboard.send('ctrl+a')
    keyboard.send('tab')
    keyboard.send('shift+tab')



keyboard.add_hotkey('ctrl+v', foo)
keyboard.wait('ctrl+q')
