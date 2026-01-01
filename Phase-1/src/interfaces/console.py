from typing import Optional
from src.services.todo_list import TodoList


class ConsoleInterface:
    """
    Handles user input/output and command parsing.
    """

    def __init__(self, todo_list: TodoList):
        """
        Initialize the console interface.

        Args:
            todo_list: The TodoList service instance to interact with
        """
        self.todo_list = todo_list

    def parse_command(self, user_input: str) -> tuple:
        """
        Parse user input into command and arguments.

        Args:
            user_input: Raw input from the user

        Returns:
            A tuple containing (command, args) or (None, None) if invalid
        """
        if not user_input.strip():
            return None, None

        parts = user_input.strip().split()
        if not parts:
            return None, None

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Handle commands that need to keep the rest as a single string
        if command in ['add', 'update'] and len(parts) > 1:
            # For add/update, the description might contain spaces
            full_text = user_input.strip()[len(command):].strip()
            if full_text.startswith('"') and full_text.endswith('"') and len(full_text) > 1:
                # Handle quoted strings
                full_text = full_text[1:-1]  # Remove surrounding quotes
            elif command == 'add':
                # For add command, treat everything after 'add' as the description
                full_text = user_input.strip()[3:].strip()  # Remove 'add' and leading/trailing spaces
            args = [full_text]

        return command, args

    def execute_command(self, command: str, args: list) -> str:
        """
        Execute the parsed command.

        Args:
            command: The command to execute
            args: Arguments for the command

        Returns:
            Result message to display to the user
        """
        if command == 'add':
            if len(args) < 1 or not args[0].strip():
                return "Error: Please provide a description for the task."
            description = args[0].strip()
            try:
                item_id = self.todo_list.add_item(description)
                return f"Added task #{item_id}: {description}"
            except ValueError as e:
                return f"Error: {str(e)}"

        elif command == 'list':
            items = self.todo_list.get_all_items()
            if not items:
                return "Your todo list is empty."

            result = []
            for item in items:
                result.append(str(item))
            return "\n".join(result)

        elif command == 'update':
            if len(args) < 2:
                return "Error: Please provide both ID and new description. Usage: update <id> <new description>"

            try:
                item_id = int(args[0])
            except ValueError:
                return f"Error: Invalid ID '{args[0]}'. Please provide a valid number."

            new_description = args[1]
            try:
                if self.todo_list.update_item(item_id, new_description):
                    return f"Updated task #{item_id}: {new_description}"
                else:
                    return f"Error: Task with ID {item_id} not found."
            except ValueError as e:
                return f"Error: {str(e)}"

        elif command == 'delete':
            if len(args) < 1:
                return "Error: Please provide an ID. Usage: delete <id>"

            try:
                item_id = int(args[0])
            except ValueError:
                return f"Error: Invalid ID '{args[0]}'. Please provide a valid number."

            if self.todo_list.delete_item(item_id):
                return f"Deleted task #{item_id}"
            else:
                return f"Error: Task with ID {item_id} not found."

        elif command in ['complete', 'incomplete']:
            if len(args) < 1:
                return f"Error: Please provide an ID. Usage: {command} <id>"

            try:
                item_id = int(args[0])
            except ValueError:
                return f"Error: Invalid ID '{args[0]}'. Please provide a valid number."

            if command == 'complete':
                if self.todo_list.mark_complete(item_id):
                    return f"Marked task #{item_id} as complete"
                else:
                    return f"Error: Task with ID {item_id} not found."
            else:  # incomplete
                if self.todo_list.mark_incomplete(item_id):
                    return f"Marked task #{item_id} as incomplete"
                else:
                    return f"Error: Task with ID {item_id} not found."

        elif command == 'help':
            return self.get_help_text()

        elif command in ['exit', 'quit']:
            return "exit"  # Special return to indicate exit

        else:
            return f"Error: Unknown command '{command}'. Type 'help' for available commands."

    def get_help_text(self) -> str:
        """
        Return help text with available commands.

        Returns:
            Formatted help text
        """
        return """Available commands:
- add "description"     : Add a new todo item
- list                : View all todo items
- update <id> "desc"  : Update a todo item
- delete <id>         : Delete a todo item
- complete <id>       : Mark item as complete
- incomplete <id>     : Mark item as incomplete
- help                : Show this help message
- exit/quit           : Exit the application"""

    def handle_user_input(self, user_input: str) -> str:
        """
        Process user input and return appropriate response.

        Args:
            user_input: Raw user input

        Returns:
            Response to display to the user
        """
        command, args = self.parse_command(user_input)

        if command is None:
            return "Error: Please enter a command. Type 'help' for available commands."

        return self.execute_command(command, args)