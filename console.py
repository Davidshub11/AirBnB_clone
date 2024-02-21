#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import shlex
import re
from models.engine.file_storage import FileStorage
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
        commands = arg.split()
        
        
        if len(commands) == 0:
            print("** class name missing **")
            return
        elif len(commands) == 1:
            print("** instance id missing **")
            return
        elif len(commands) == 2:
            print("** attribute name missing **")
            return
        elif len(commands) == 3:
            print("** value missing **")
            return

        class_name = commands[0]
        instance_id = commands[1]
        attribute_name = commands[2]
        attribute_value = ' '.join(commands[3:])
        print("cN= {}, I_ID = {}, att_Name = {}, att_value = {}".format(class_name, instance_id, attribute_name,  attribute_value))

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)

        print(objects)
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

        if arg:
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

        incoming_extra_arg = command[1].split(')')[0]

        # Split the incoming_extra_arg by commas to get individual arguments
        all_args = incoming_extra_arg.split(',')

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
        }

        if incoming_method in method_dict.keys():
            if incoming_method != "update":
                return method_dict[incoming_method]("{} {}".format(
                        incoming_class_name, incoming_extra_arg))
            else:
                # For the "update" method, extract individual arguments
                if len(all_args) < 3:
                    print("** value missing **")
                    return False

                obj_id = all_args[0].strip()
                attribute_name = all_args[1].strip()
                attribute_value = ','.join(all_args[2:])
                print(" This is ATT_value :", attribute_value)

                return method_dict[incoming_method]("{} {} {}".format(
                        incoming_class_name, obj_id,
                        attribute_name, attribute_value))

        else:
            print("** Unknown syntax: {}".format(arg))
            return False



if __name__ == "__main__":
    HBNBCommand().cmdloop()
