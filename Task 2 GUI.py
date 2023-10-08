# TASK 2: CALCULATOR - GUI

from tkinter import *


def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
    except ValueError:
        result_label.config(text='Invalid input. Please enter a number.')
        return

    choice = operation_var.get()

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            result_label.config(text='Cannot divide by zero.')
            return
        result = num1 / num2
    elif choice == '5':
        if num2 == 0:
            result_label.config(text='Cannot perform modulus by zero.')
            return
        result = num1 % num2
    else:
        result_label.config(text='Invalid choice.')
        return

    result_label.config(text=f'Result: {result}')


root = Tk()
root.title('Simple Calculator')

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text='Enter the first number:').grid(row=0, column=0)
num1_entry = Entry(frame, width=20)
num1_entry.grid(row=0, column=1)

Label(frame, text='Enter the second number:').grid(row=1, column=0)
num2_entry = Entry(frame, width=20)
num2_entry.grid(row=1, column=1)

operation_var = StringVar()
operation_var.set('1')

Label(frame, text='Select operation:').grid(row=2, column=0)
Radiobutton(frame, text='Add', variable=operation_var, value='1').grid(row=2, column=1, sticky=W)
Radiobutton(frame, text='Subtract', variable=operation_var, value='2').grid(row=3, column=1, sticky=W)
Radiobutton(frame, text='Multiply', variable=operation_var, value='3').grid(row=4, column=1, sticky=W)
Radiobutton(frame, text='Divide', variable=operation_var, value='4').grid(row=5, column=1, sticky=W)
Radiobutton(frame, text='Modulus', variable=operation_var, value='5').grid(row=6, column=1, sticky=W)

Button(frame, text='Calculate', command=calculate).grid(row=7, columnspan=2)

result_label = Label(frame, text='')
result_label.grid(row=8, columnspan=2)

root.mainloop()
