"""
Приложение hello world на Tkinter
"""
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Hello world app')
window.geometry('200x100')


def say_hello():
    print('HELLO WORLD')


hello_button = ttk.Button(window, text='Say Hello', command=say_hello)
hello_button.pack()

window.mainloop()
