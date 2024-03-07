#!/usr/bin/python3

"""
Program ``console.py`` contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


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

    def do_create(self, arg):
        """
        Create a new instance of a class
        """

        class_name = arg.strip().lower()

        if not class_name:
            print("** class name missing **")
        elif class_name not in ["basemodel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """
        Documentation for ``create``
        """
        print("``create`` creates a model and accepts the name of model as arg")

    def do_show(self, arg):
        """
        prints a string rep of an instance
        """

        arg_list = arg.split(' ')
        
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0].lower() not in ['basemodel']:
            print("** class doesn't exist **")
        elif len(arg_list) != 2:
            print("** instance id missing **")
        else:
            obj_found = None
            all_objects = storage.all()

            for key, value in all_objects.items():

                if value['__class__'].lower() == arg_list[0].lower():

                    if value['id'] == arg_list[1]:

                        obj_found = value
                        break
            if obj_found:
                new_instance = BaseModel(**value)
                print(new_instance)
            else:
                print("** no instance found **")

    def help_show(self, arg):
        """
        Documentation for ``show``
        """
        print("``show`` display an obj if it exist. Usage: ``show (classname) (id)``")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        """

        arg_list = arg.split(' ')
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0].lower() not in ['basemodel']:
            print("** class doesn't exist **")
        elif len(arg_list) != 2:
            print("** instance id missing **")
        else:
            obj_found = None
            all_objects = storage.all()

            for key, value in all_objects.items():
                if value['__class__'].lower() == arg_list[0].lower():
                    if value['id'] == arg_list[1]:

                        obj_found = key
                        break
            if obj_found:
                del all_objects[obj_found]
            else:
                pass # Should I use the file name directly since I know it?

    def emptyline(self):
        """
        Handle empty line.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
