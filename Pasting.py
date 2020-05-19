from keyboard import write, add_hotkey, wait
from time import sleep
from pyperclip import paste

def foo():
    clip = paste()
    clip = clip.split('\n')
    for i in clip:
        write(i)
        sleep(0.1)

add_hotkey('ctrl+v', foo)
wait('ctrl+q')
