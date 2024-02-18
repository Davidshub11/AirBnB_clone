#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]

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
            new_instance = BaseModel()
            new_instance.save()
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
            print("** class doesen't exist **")
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
            update an instance by adding or update an attribute.
            Usage: update <class_name> <id> <attribute_name>
            "<attribute_value>"
            """
            commands = shlex.split(arg)

            if len(commands) == 0:
                print("** class name missing **")
            elif commands[0] not in self.valid_classes:
                print(" ** class doesnt't exist **")
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
