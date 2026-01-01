from typing import Dict, List, Optional
from src.models.todo_item import TodoItem


class TodoList:
    """
    Manages collection of TodoItems with CRUD operations.
    """

    def __init__(self):
        """
        Initialize an empty todo list.
        """
        self.items: Dict[int, TodoItem] = {}
        self.next_id = 1

    def add_item(self, description: str) -> int:
        """
        Add a new todo item and return its ID.

        Args:
            description: Description of the todo item

        Returns:
            ID of the newly created todo item
        """
        # Validate description length to prevent extremely long entries
        if len(description) > 1000:  # Limit to 1000 characters
            raise ValueError("Description is too long. Maximum 1000 characters allowed.")

        item = TodoItem(self.next_id, description)
        self.items[self.next_id] = item
        item_id = self.next_id
        self.next_id += 1
        return item_id

    def get_item(self, item_id: int) -> Optional[TodoItem]:
        """
        Retrieve a todo item by ID.

        Args:
            item_id: ID of the todo item to retrieve

        Returns:
            TodoItem if found, None otherwise
        """
        return self.items.get(item_id)

    def update_item(self, item_id: int, new_description: str) -> bool:
        """
        Update an existing todo item.

        Args:
            item_id: ID of the todo item to update
            new_description: New description for the item

        Returns:
            True if update was successful, False otherwise
        """
        if item_id not in self.items:
            return False
        if not new_description or not new_description.strip():
            return False  # Cannot update with empty description
        # Validate description length to prevent extremely long entries
        if len(new_description) > 1000:  # Limit to 1000 characters
            raise ValueError("Description is too long. Maximum 1000 characters allowed.")
        self.items[item_id].update_description(new_description)
        return True

    def delete_item(self, item_id: int) -> bool:
        """
        Remove a todo item by ID.

        Args:
            item_id: ID of the todo item to remove

        Returns:
            True if deletion was successful, False otherwise
        """
        if item_id not in self.items:
            return False
        del self.items[item_id]
        return True

    def mark_complete(self, item_id: int) -> bool:
        """
        Mark a todo item as complete.

        Args:
            item_id: ID of the todo item to mark complete

        Returns:
            True if marking was successful, False otherwise
        """
        if item_id not in self.items:
            return False
        self.items[item_id].mark_complete()
        return True

    def mark_incomplete(self, item_id: int) -> bool:
        """
        Mark a todo item as incomplete.

        Args:
            item_id: ID of the todo item to mark incomplete

        Returns:
            True if marking was successful, False otherwise
        """
        if item_id not in self.items:
            return False
        self.items[item_id].mark_incomplete()
        return True

    def get_all_items(self) -> List[TodoItem]:
        """
        Return all todo items.

        Returns:
            List of all TodoItem objects
        """
        return list(self.items.values())

    def get_completed_items(self) -> List[TodoItem]:
        """
        Return only completed items.

        Returns:
            List of completed TodoItem objects
        """
        return [item for item in self.items.values() if item.completed]

    def get_pending_items(self) -> List[TodoItem]:
        """
        Return only pending items.

        Returns:
            List of pending TodoItem objects
        """
        return [item for item in self.items.values() if not item.completed]