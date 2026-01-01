# Data Model: Console Todo Application

## TodoItem Entity

**Description**: Represents a single todo item with properties and methods

**Fields**:
- `id`: Unique identifier (integer)
- `description`: Text description of the task (string)
- `completed`: Boolean indicating completion status (boolean)
- `created_at`: Timestamp of creation (datetime)

**Methods**:
- `__init__(id, description)`: Initialize a new todo item
- `mark_complete()`: Mark the item as complete
- `mark_incomplete()`: Mark the item as incomplete
- `update_description(new_description)`: Update the item description

## TodoList Entity

**Description**: Manages collection of TodoItems with CRUD operations

**Fields**:
- `items`: Collection of TodoItem objects (dictionary with id as key)
- `next_id`: Counter for generating unique IDs (integer)

**Methods**:
- `__init__()`: Initialize an empty todo list
- `add_item(description)`: Add a new todo item and return its ID
- `get_item(id)`: Retrieve a todo item by ID
- `update_item(id, new_description)`: Update an existing todo item
- `delete_item(id)`: Remove a todo item by ID
- `mark_complete(id)`: Mark a todo item as complete
- `mark_incomplete(id)`: Mark a todo item as incomplete
- `get_all_items()`: Return all todo items
- `get_completed_items()`: Return only completed items
- `get_pending_items()`: Return only pending items