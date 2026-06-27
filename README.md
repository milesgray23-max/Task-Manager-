# Task-Manager-
A desktop task management application built with Python and Tkinter. This app allows users to create, manage, and track tasks with saved data storage.
# Task Manager - Python

## Features

- Add tasks
- Delete tasks
- Mark tasks as completed
- Set task priority levels
- Add due dates
- Save tasks automatically using JSON
- Load saved tasks when reopening the application
- User-friendly GUI interface

## Technologies Used

- Python
- Tkinter (GUI)
- JSON (Data Storage)

## How It Works

Tasks are stored in a JSON file so the information remains saved after closing the application.

Each task contains:

- Task name
- Priority level
- Due date
- Completion status

Example:

```json
{
    "task": "Finish Python project",
    "priority": "High",
    "due": "Friday",
    "completed": false
}
