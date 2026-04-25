import numpy as np
from random import randint
import tkinter as tk
import ttkbootstrap as ttk

root = ttk.Window(themename='darkly')
root.geometry('500x500')
root.title('random word generator')

text = tk.StringVar(value='')
word_length = tk.IntVar(value=5)

alphabet = np.array(
    [
    [['a','b','c'], 
    ['d','e','f'],
    ['g','h','i']],

    [['j','k','l'],
    ['m','n','o'],
    ['p','q','r']],

    [['s','t','u'],
    ['v','w','x'],
    ['y','z',' ']]
    ]
)

def random_word():
    text.set('')
    try:
        for i in range(0,word_length.get()):
            text.set(text.get() + (alphabet[randint(0,2),randint(0,2),randint(0,2)]))

    except:
        text.set('error')

display = ttk.Label(root,textvariable=text, font='Kalinga 25 bold')
length_frame = ttk.Frame(root)
length_label = ttk.Label(length_frame, text='word length:')
word_length_input = ttk.Entry(length_frame, textvariable=word_length)
select_rand_word = ttk.Button(root,text='create', command=random_word)

display.pack()
length_frame.pack(pady=10)
length_label.pack(side='top')
word_length_input.pack(side='right')
select_rand_word.pack()

tk.mainloop()
