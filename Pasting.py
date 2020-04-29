import keyboard #библиотека для управления клавиатурой, в частности установка хоткеев
from tkinter import Tk # библиотека, которая здесь получает значение буфера обмена в переменную

def foo():
    c = Tk() # инициалиция объекта
    c.withdraw() # удаление окна библиотеки
    clip = c.clipboard_get() # получение данных
    c.update()
    c.destroy() # обновление и удаление объекта
    keyboard.write(clip) # печать переменной

keyboard.add_hotkey('ctrl+v', foo) # добавление хоткея
keyboard.wait('ctrl+q') # добавление хоткея на завершение прогаммы
