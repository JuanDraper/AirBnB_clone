#!/usr/bin/python3
"""console program"""

import cmd
import shlex
import models
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """console class"""

    prompt =  "(hbnb)"

    def do_quit(self, args):
        """command that quits program"""
        return True

    def do_EOF(self, args):
        """command that handles ctrl+D"""
        return True
    
    def emptyline(self):
        """makinig that an empty line  doesn´t execute anything"""
        pass
    
    def do_create(self, args):
        """command that creates instances of a given class"""
        args = shlex.split(args)
        if args ==[]:
            print("**class name missing**")
        elif args[0] not in ["BaseModel","User", "City", "Review", "Place",
                            "State", "Amenity"]:
            print("**class doesn´t exist**")
        else:
            models.storage.reload()
            n = eval(args[0])()
            n.save()
            print(n.id)

    def do_show(self, args):
        """prints the instance´s string representation"""
        args = shlex.split(args)
        if args ==[]:
            print("**class name missing**")
        elif args[0] not in ["BaseModel","User", "City", "Review", "Place",
                            "State", "Amenity"]:
            print("**class doesn´t exist**")
        elif len(args) == 1:
            print("**instance id is missing**")
        else:
            models.storage.reload()
            for i, obj in models.storage.all().items():
                if obj.id == arg[1] and obj.__class__.__name__ == arg[0]:
                    print(obj.__str__())
                    return
            print("**no instance found**")

    def do_destroy(self, args):
        """given an instance name and id, it will ve eliminated"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State",
                             "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            instances = models.storage.all()
            for i, obj in instances.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(instances[i])
                    return
            print("**no instance found**")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
