#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self, arg):
        """
        Shows all the attribute of quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Quits command interpreter with ctrl+d
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
