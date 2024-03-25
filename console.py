#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all(class_name)
            key = "{}.{}".format(class_name, args[1])
            if key not in instances:
                print("** no instance found **")
                return
            print(instances[key])
        except Exception as e:
            print(e)

    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
