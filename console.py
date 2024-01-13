#!/ucsr/bin/python3
"""
"""
import cmd
import shlex
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
    """
    prompt = "(hbnb)"
    valid_obj = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

    def do_quit(self, arg):
        """
        Quit the program
        """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def emptyline(self):
        """
        """
        pass

    def do_create(self, arg):
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
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_obj:
            print("** class doesnt exist **")
        elif len(commands) < 2:
            print(" **instance id missing** ")
        else:
            object = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance is found **")

    def do_destroy(self, arg):
        """
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
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_obj:
            print("** class doesn't exist **")
        else:
            for key, value in onjects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
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
            if key not in objects:
                print("**  no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("**value missing**")
            else:
                obj = objects[key]

                attr_name = command[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
