#!/usr/bin/python3
"""The HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """The HBNBCommand Class.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
