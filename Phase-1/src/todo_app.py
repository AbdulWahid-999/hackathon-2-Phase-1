#!/usr/bin/env python3
"""
Main application entry point for the console todo application.
"""

from src.services.todo_list import TodoList
from src.interfaces.console import ConsoleInterface


def main():
    """
    Main function to run the todo application.
    """
    print("Welcome to the Console Todo Application!")
    print("Type 'help' for available commands or 'exit' to quit.")

    # Initialize the todo list and console interface
    todo_list = TodoList()
    console = ConsoleInterface(todo_list)

    # Main application loop
    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            result = console.handle_user_input(user_input)

            if result == "exit":
                print("Goodbye!")
                break
            else:
                print(result)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()