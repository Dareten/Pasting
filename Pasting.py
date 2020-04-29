import keyboard
from tkinter import Tk

def foo():
    c = Tk()
    c.withdraw()
    clip = c.clipboard_get()
    c.update()
    c.destroy()
    keyboard.write(clip)

keyboard.add_hotkey('ctrl+v', foo)
keyboard.wait('ctrl+q')
