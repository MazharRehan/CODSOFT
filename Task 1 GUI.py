# TASK 1: TO-DO LIST - GUI

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime


def add_task():
    task_description = task_entry.get()
    task_date = cal.get_date()
    task_time = time_var.get()
    task_datetime_str = f'{task_date} {task_time}'
    try:
        task_datetime = datetime.strptime(task_datetime_str, '%m/%d/%y %H:%M')
        current_datetime = datetime.now()
        if task_datetime < current_datetime:
            error_label.config(text='Cannot add tasks with past dates.')
            return
        tasks.append({'description': task_description, 'completed': False, 'datetime': task_datetime})
        update_task_list()
    except ValueError:
        error_label.config(text='Invalid date and time format.')


def update_task_list():
    task_list.delete(0, END)
    for index, task in enumerate(tasks):
        status = '[x]' if task['completed'] else '[ ]'
        task_list.insert(END,
                         f"{index + 1}. {status} {task['description']} (Due: {task['datetime'].strftime('%Y-%m-%d %H:%M')})")


def mark_complete():
    selected_task_index = task_list.curselection()[0]
    tasks[selected_task_index]['completed'] = True
    update_task_list()


def delete_task():
    selected_task_index = task_list.curselection()[0]
    del tasks[selected_task_index]
    update_task_list()


tasks = []

root = Tk()
root.title('To-Do List App')

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text='Task Description:').grid(row=0, column=0)
task_entry = Entry(frame, width=50)
task_entry.grid(row=0, column=1)

Label(frame, text='Due Date:').grid(row=1, column=0)
cal = Calendar(frame, selectmode='day')
cal.grid(row=1, column=1)

Label(frame, text='Due Time:').grid(row=2, column=0)
time_var = StringVar()
time_entry = ttk.Combobox(frame, textvariable=time_var,
                          values=[f'{h:02d}:{m:02d}' for h in range(24) for m in range(0, 60, 5)], width=47)
time_entry.grid(row=2, column=1)

Button(frame, text='Add Task', command=add_task).grid(row=3, columnspan=2)

error_label = Label(frame, text='', fg='red')
error_label.grid(row=4, columnspan=2)

task_list = Listbox(root, width=100, height=15, selectmode=SINGLE)
task_list.pack(pady=10)

Button(root, text='Mark as Complete', command=mark_complete).pack(side=LEFT, padx=10)
Button(root, text='Delete Task', command=delete_task).pack(side=RIGHT, padx=10)

root.mainloop()
