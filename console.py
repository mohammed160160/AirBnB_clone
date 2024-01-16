#!/usr/bin/python3
"""
Console Module
"""
import cmd
import shlex
import json
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNB command console class
    """
    prompt = "(hbnb)"
    valid_obj = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                 "City": City, "Place": Place, "Review": Review,
                 "State": State}

    def do_quit(self, arg):
        """
        Quit the program
        """
        return True

    def help_quit(self, arg):
        """
        Show quit info/Usage
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Ctrl+D signal to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing in case of an empty line
        """
        pass

    def default(self, line):
        """
        Tweak default Operation
        """
        arg_list = line.split('.')
        arg_command = arg_list[0]
        dot_method = arg_list[1]
        isee_method = dot_method.split('(')
        arg_method = isee_method[0]

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }

        if arg_method in method_dict.keys():
            return method_dict[arg_method]("{} {}".format(arg_command, ''))

        print("** Unknown syntax: {}".format(line))
        return False

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_obj:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show str reprensentation
        of an instance
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_obj:
            print("** class doesnt exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete and instance instance using classname/id
        Usage: destro <class name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_obj:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print String representation of all instances or
        a specific class
        Usage: <User>.all()
        """

        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_obj:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_obj:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class.
        """
        commands = shlex.split(arg)

        if arg:
            first_arg = commands[0]
            count = 0

        if commands:
            if first_arg in self.valid_obj:
                objects = storage.all()

                for obj in objects.values():
                    if obj.__class__.__name__ == first_arg:
                        count += 1
                print(count)
            else:
                print("** invaliid shit **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
