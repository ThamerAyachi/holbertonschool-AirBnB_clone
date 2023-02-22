#!/usr/bin/python3
"""Entry point of Console"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand (cmd.Cmd):
    """Console class"""

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        '''Prevents repeat of previous input.'''
        pass

    def do_create(self, line):
        """Create new Module"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            model = self.classes[line]()
            print(model.id)

    def do_show(self, line):
        """Show model by name and id"""
        if not line:
            print("** class name missing **")
        elif len(line.split(" ")) != 2:
            print("** instance id missing **")
        else:
            model_name = line.split(" ")[0]
            model_id = line.split(" ")[1]
            if model_name not in self.classes:
                print("** class doesn't exist **")
            else:
                models.storage.reload()
                my_dict = models.storage.all()
                if model_id not in str(my_dict):
                    print("** no instance found **")
                else:
                    print(my_dict[f"{model_name}.{model_id}"])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id,'''
        args = arg.split()

        if (len(args) == 0):
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            if args[0] in self.classes:
                models.storage.reload()
                new_dict = models.storage.all()
                if args[1] not in str(new_dict):
                    print("** no instance found **")
                else:
                    del new_dict[f"{args[0]}.{args[1]}"]
                    models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
