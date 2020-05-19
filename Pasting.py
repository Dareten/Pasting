import keyboard
import time
import pyperclip

def foo():
    clip = pyperclip.paste()
    clip = clip.split('\n')
    for i in clip:
        keyboard.write(i)
        time.sleep(0.1)

keyboard.add_hotkey('ctrl+v', foo)
keyboard.wait('ctrl+q')
