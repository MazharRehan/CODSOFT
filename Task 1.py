""" TASK 1: TO-DO LIST - CONSOLE
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
"""

from datetime import datetime

# Define an empty list to store tasks
tasks = []

# Function to clear the console screen
def clear_screen():
    print('\n' * 100)

# Function to add a task
def add_task():
    clear_screen()
    task_description = input("Enter task description: ")
    task_datetime_str = input("Enter task due date and time (YYYY-MM-DD HH:MM): ")

    try:
        task_datetime = datetime.strptime(task_datetime_str, "%Y-%m-%d %H:%M")
        tasks.append({"description": task_description, "completed": False, "datetime": task_datetime})
        print("Task added successfully!")
    except ValueError:
        print("Invalid date and time format. Task not added.")

# Function to view tasks
def view_tasks():
    clear_screen()
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = " [x] " if task["completed"] else " [ ] "
            print(f"{index + 1}.{status}{task['description']} (Due: {task['datetime'].strftime('%Y-%m-%d %H:%M')})")

# Function to mark a task as complete
def mark_complete():
    clear_screen()
    view_tasks()
    task_index = int(input("Enter the task number to mark as complete (0 to cancel): ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    elif task_index == -1:
        pass
    else:
        print("Invalid task number.")

# Function to edit a task
def edit_task():
    clear_screen()
    view_tasks()
    task_index = int(input("Enter the task number to edit (0 to cancel): ")) - 1
    if 0 <= task_index < len(tasks):
        new_description = input("Enter new task description: ")
        new_datetime_str = input("Enter new due date and time (YYYY-MM-DD HH:MM): ")

        try:
            new_datetime = datetime.strptime(new_datetime_str, "%Y-%m-%d %H:%M")
            tasks[task_index]["description"] = new_description
            tasks[task_index]["datetime"] = new_datetime
            print("Task edited successfully!")
        except ValueError:
            print("Invalid date and time format. Task not edited.")
    elif task_index == -1:
        pass
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task['description']}' deleted successfully!")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    clear_screen()
    print("Welcome to the To-Do List App!")
    # Main loop for the program
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
            input("Press Enter to continue...")
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            clear_screen()
            print("Goodbye!")
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")