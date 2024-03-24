#!/usr/bin/python3
from models.base_model import BaseModel
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
