#!/usr/bin/python3

"""
Program ``console.py`` contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.__init__ import storage
import json
import shlex
from models.user import User


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
        elif class_name not in [
                "basemodel",
                "user",
                "place",
                "state",
                "city",
                "amenity",
                "review"
                ]:
            print("** class doesn't exist **")
        else:
            if class_name == "user":
                new_instance = User()
            elif class_name == "place":
                new_instance = Place()
            elif class_name == "state":
                new_instance = State()
            elif class_name == "city":
                new_instance = City()
            elif class_name == "review":
                new_instance = Review()
            elif class_name == "amenity":
                new_instance = Amenity()
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

        arg_list = arg.split(" ")

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0].lower() not in [
            "basemodel",
            "user",
            "place",
            "city",
            "amenity",
            "review",
        ]:
            print("** class doesn't exist **")
        elif len(arg_list) != 2:
            print("** instance id missing **")
        else:
            obj_found = None
            all_objects = storage.all()

            for key, value in all_objects.items():
                if value["__class__"].lower() == arg_list[0].lower():
                    if value["id"] == arg_list[1]:
                        obj_found = value
                        break
            if obj_found:
                class_name = obj_found["__class__"].lower()

                if class_name == "user":
                    new_instance = User(**value)
                elif class_name == "place":
                    new_instance = Place(**value)
                elif class_name == "city":
                    new_instance = City(**value)
                elif class_name == "amenity":
                    new_instance = Amenity(**value)
                elif class_name == "review":
                    new_instance = Review(**value)
                else:
                    new_instance = BaseModel(**value)
                print(new_instance)
            else:
                print("** no instance found **")

    def help_show(self):
        """
        Documentation for ``show``
        """
        print("``show`` display an obj if it exist. Usage: ``show (classname) (id)``")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        """

        arg_list = arg.split(" ")
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0].lower() not in [
                "basemodel",
                "user",
                "place",
                "state",
                "city",
                "amenity",
                "review"
                ]:
            print("** class doesn't exist **")
        elif len(arg_list) != 2:
            print("** instance id missing **")
        else:
            obj_found = None
            all_objects = storage.all()

            for key, value in all_objects.items():
                if value["__class__"].lower() == arg_list[0].lower():
                    if value["id"] == arg_list[1]:
                        obj_found = key
                        break
            if obj_found:
                del all_objects[obj_found]

                with open("file.json", "w", encoding="utf-8") as f:
                    json.dump(all_objects, f, indent=4, sort_keys=True)
            else:
                print("** no instance found **")

    def help_destroy(self):
        """
        Documentation for ``destroy``
        """
        print("`destroy` deletes an obj. Usage: `destroy` (classname) (id)``")

    def do_all(self, arg):
        """
        Prints all string rep of all instances
        """
        new_list = []

        if len(arg) == 0:
            all_objects = storage.all()

            for key, value in all_objects.items():
                class_name = value["__class__"].lower()

                if class_name == "user":
                    new_instance = User(**value)
                elif class_name == "place":
                    new_instance = Place(**value)
                elif class_name == "state":
                    new_instance = State(**value)
                elif class_name == "amenity":
                    new_instance = Amenity(**value)
                elif class_name == "review":
                    new_instance = Review(**value)
                else:
                    new_instance = BaseModel(**value)
                new_list.append(str(new_instance))

        elif arg is not None:
            if arg.strip().lower() not in ["basemodel", "user", "place", "state", "amenity", "review"]:
                print("** class doesn't exist **")
            else:
                all_objects = storage.all()

                for key, value in all_objects.items():
                    class_name = value["__class__"].lower()

                    if class_name == arg.strip().lower():
                        if class_name == "user":
                            new_instance = User(**value)
                        elif class_name == "place":
                            new_instance = Place(**value)
                        elif class_name == "state":
                            new_instance = State(**value)
                        elif class_name == "amenity":
                            new_instance = Amenity(**value)
                        elif class_name == "review":
                            new_instance = Review(**value)
                        else:
                            new_instance = BaseModel(**value)
                        new_list.append(str(new_instance))
        print(new_list)

    def help_all(self):
        """
        Documentation for all command
        """
        print("`all`: used to print objs in list")

    def do_update(self, arg):
        """
        Updates an instance based on classname and id
        """

        arg_list = arg.split(" ")
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0].lower() not in [
                "basemodel",
                "user",
                "place",
                "state",
                "city",
                "amenity",
                "review"
                ]:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_found = False
            all_objects = storage.all()

            for key, value in all_objects.items():
                if value["__class__"].lower() == arg_list[0].lower():
                    if value["id"] == arg_list[1]:
                        obj_found = True
                        obj_value = value
                        break
            if obj_found is False:
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                obj_value[arg_list[2]] = shlex.split(arg_list[3])[0]

                with open("file.json", "w", encoding="utf-8") as f:
                    json.dump(all_objects, f, indent=4, sort_keys=True)

    def help_update(self):
        """
        Documentation for `update` command
        """
        print("update an attribute in an obj")
        print('Usage: <class name> <id> <attr name> "<attr value>"')

    def emptyline(self):
        """
        Handle empty line.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
