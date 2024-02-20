#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
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
    Custom console class
    """

    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Quits command interpreter with ctrl+d
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """
        create a new instance of BaseModel and save it to the Json file.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** Class name missing**")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print(" ** instance id missing ** ")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesen't exist **")
        elif len(commands) < 2:
            print(" ** instance id missing ** ")
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
        print the string representation of all instances or a specific class
        usage: all[class_name]
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesen't exist **")
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
            return
        elif len(commands) < 2:
            print("** instance id missing **")
            return
        elif len(commands) < 3:
            print("** attribute name missing **")
            return
        elif len(commands) < 4:
            print("** value missing **")
            return

        class_name = commands[0]
        instance_id = commands[1]
        attribute_name = commands[2]
        attribute_value = ' '.join(commands[3:])

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in objects:
            print("** no instance found **")
            return

        obj = objects[key]

        try:
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        except Exception as e:
            pass

    def do_count(self, arg):
        """
        Counts and retrieve the number of instances of a class
        Usage: <class name>.count().
        """
        objects = storage.all()
        command = shlex.split(arg)

        incoming_class_name = command[0]

        count = 0

        if command:
            if incoming_class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == incoming_class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def default(self, arg):
        """
        Default behavior for cmd module for invalid syntax
        """
        arg_list = arg.split('.')
        incoming_class_name = arg_list[0]

        command = arg_list[1].split('(')
        incoming_method = command[0]

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
        }
        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{} {}".format(
                incoming_class_name, ""))

        else:
            print("** Unknown syntax: {}".format(arg))
            return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
