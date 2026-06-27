import tkinter as tk
import json


tasks = []

def save_tasks():

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks():

    global tasks

    try:

        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:

        tasks = []


def add_task():

    task = task_entry.get()

    priority = priority_entry.get()

    due = due_entry.get()


    new_task = {

        "task": task,

        "priority": priority,

        "due": due,

        "completed": False
    }


    tasks.append(new_task)

    save_tasks()


    task_list.insert(
        tk.END,
        f"{task} | {priority} | {due}"
    )


    task_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)

def delete_task():

    selected = task_list.curselection()

    if selected:

        index = selected[0]

        tasks.pop(index)

        save_tasks()

        task_list.delete(index)

def complete_task():

    selected = task_list.curselection()

    if selected:

        index = selected[0]


        tasks[index]["completed"] = True


        save_tasks()


        task_list.delete(index)


        task_list.insert(
            index,
            f"✔ {tasks[index]['task']} | {tasks[index]['priority']} | {tasks[index]['due']}"
        )

load_tasks()

window = tk.Tk()

window.title("Task Manager")

window.geometry("400x400")


task_entry = tk.Entry(window)

task_entry.pack()

due_label = tk.Label(
    window,
    text="Due Date"
)

due_label.pack()

due_entry = tk.Entry(window)

due_entry.pack()

priority_label = tk.Label(
    window,
    text="Priority"
)

priority_label.pack()


priority_entry = tk.Entry(window)

priority_entry.pack()

add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task
)

add_button.pack()


task_list = tk.Listbox(window)

task_list.pack()

for task in tasks:

    task_list.insert(
        tk.END,
        f"{task['task']} | {task['priority']} | {task['due']}"
    )


delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task
)

delete_button.pack()

complete_button = tk.Button(
    window,
    text="Complete Task",
    command=complete_task
)

complete_button.pack()

window.mainloop()
