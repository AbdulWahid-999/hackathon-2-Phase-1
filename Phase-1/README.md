# Console Todo Application

A simple console-based todo application built with Python.

## Features

- Add new todo items
- View all todo items
- Update existing todo items
- Delete todo items
- Mark items as complete/incomplete

## Requirements

- Python 3.13+
- UV package manager

## Installation

1. Clone or download the project
2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Usage

Run the application:

```bash
uv run -m src.todo_app
```

Or install and run as a package:

```bash
uv pip install -e .
todo-app
```

### Available Commands

- `add "description"`     : Add a new todo item
- `list`                : View all todo items
- `update <id> "desc"`  : Update a todo item
- `delete <id>`         : Delete a todo item
- `complete <id>`       : Mark item as complete
- `incomplete <id>`     : Mark item as incomplete
- `help`                : Show this help message
- `exit/quit`           : Exit the application

### Example Usage

```
> add "Buy groceries"
Added task #1: Buy groceries

> list
1. [ ] Buy groceries

> complete 1
Marked task #1 as complete

> list
1. [x] Buy groceries

> exit
Goodbye!
```

## Project Structure

```
src/
├── todo_app.py          # Main application entry point
├── models/
│   ├── __init__.py
│   └── todo_item.py     # TodoItem class definition
├── services/
│   ├── __init__.py
│   └── todo_list.py     # TodoList service class
└── interfaces/
    ├── __init__.py
    └── console.py       # Console interface handler
```

## License

This project is licensed under the terms specified in the LICENSE file (to be added).