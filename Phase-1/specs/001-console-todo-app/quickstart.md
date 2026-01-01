# Quickstart Guide: Console Todo Application

## Prerequisites

- Python 3.13+ installed on your system
- UV package manager installed

## Setup

1. Clone or access the project repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is available: `python --version`

## Installation

1. Install dependencies using UV:
   ```bash
   uv pip install -r requirements.txt
   ```

   Or if no requirements.txt exists yet:
   ```bash
   # No external dependencies required for basic functionality
   ```

## Running the Application

1. Execute the main application file:
   ```bash
   python src/todo_app.py
   ```

2. The application will start in interactive mode, showing a prompt.

## Basic Usage

### Adding a Todo Item
```
> add "Buy groceries"
Added task #1: Buy groceries
```

### Viewing All Todo Items
```
> list
1. [ ] Buy groceries
2. [x] Finish report
3. [ ] Call dentist
```

### Updating a Todo Item
```
> update 1 "Buy groceries and cook dinner"
Updated task #1: Buy groceries and cook dinner
```

### Marking a Todo as Complete
```
> complete 1
Marked task #1 as complete
```

### Deleting a Todo Item
```
> delete 2
Deleted task #2
```

### Getting Help
```
> help
Available commands:
- add "description"     : Add a new todo item
- list                : View all todo items
- update <id> "desc"  : Update a todo item
- delete <id>         : Delete a todo item
- complete <id>       : Mark item as complete
- incomplete <id>     : Mark item as incomplete
- help                : Show this help message
- exit/quit           : Exit the application
```

## Exiting the Application
```
> exit
Goodbye!
```

## Troubleshooting

- If you get a "command not found" error, ensure you're running the Python file from the correct directory
- If the application crashes, check that you're providing the correct arguments to each command
- For empty descriptions or invalid IDs, the application will show helpful error messages