from datetime import datetime
from typing import Optional


class TodoItem:
    """
    Represents a single todo item with properties and methods.
    """

    def __init__(self, item_id: int, description: str, completed: bool = False):
        """
        Initialize a new todo item.

        Args:
            item_id: Unique identifier for the item
            description: Text description of the task
            completed: Boolean indicating completion status (default: False)
        """
        self.id = item_id
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()

    def mark_complete(self):
        """Mark the item as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the item as incomplete."""
        self.completed = False

    def update_description(self, new_description: str):
        """
        Update the item description.

        Args:
            new_description: New description for the item
        """
        self.description = new_description

    def __str__(self):
        """String representation of the todo item."""
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.description}"

    def to_dict(self):
        """Convert the todo item to a dictionary representation."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }