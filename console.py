#!/usr/bin/python3

"""
Program ``console.py`` contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Comand interpreter for HBNB program

    Attributes:
        prompt (str): console prompt

    Methods:
        quit() -> bool: To exit a program
        help() -> documentation of commands

    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program
        """
        print()
        return True

    def help_quit(self):
        """
        Documentation for ``quit``
        """
        print("``quit`` exits the program")

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print()
        return True

    def help_EOF(self):
        """
        Documentation for ``EOF``
        """
        print("``EOF`` | Ctrl + D exits the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
