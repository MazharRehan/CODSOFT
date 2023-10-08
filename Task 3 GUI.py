# Task 3: PASSWORD GENERATOR - GUI

import random
import string
from tkinter import *


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text='Password length should be at least 4 characters.')
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        result_label.config(text=f'Generated Password: {password}')
    except ValueError:
        result_label.config(text='Invalid input. Please enter a number.')


root = Tk()
root.title('Password Generator')

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text='Enter the desired length of the password:').grid(row=0, column=0)
length_entry = Entry(frame, width=20)
length_entry.grid(row=0, column=1)

Button(frame, text='Generate Password', command=generate_password).grid(row=1, columnspan=2)

result_label = Label(frame, text='')
result_label.grid(row=2, columnspan=2)

root.mainloop()
