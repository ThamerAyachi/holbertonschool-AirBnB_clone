#!/usr/bin/python3
"""Entry point of Console"""
import cmd


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
