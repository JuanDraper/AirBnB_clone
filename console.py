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

classes = ["BaseModel", "User", "City", "Review", "Place",
            "State", "Amenity"]

class HBNBCommand(cmd.Cmd):
    """console class"""

    prompt = "(hbnb)"
    
    def do_quit(self, args):
        """command that quits program"""
        return True

    def do_EOF(self, args):
        """command that handles ctrl+D"""
        return True

    def emptyline(self):
        """making that an empty line doesn´t execute anything"""
        pass

    def do_create(self, args):
        """command that creates instances of a given class"""
        args = shlex.split(args)
        if args == []:
            print("**class name missing**")
        elif args[0] not in classes:
            print("**class doesn´t exist**")
        else:
            models.storage.reload()
            n = eval(args[0])()
            n.save()
            print(n.id)

    def do_show(self, args):
        """prints the instance´s string representation"""
        args = shlex.split(args)
        if args == []:
            print("**class name missing**")
        elif args[0] not in classes:
            print("**class doesn´t exist**")
        elif len(args) == 1:
            print("**instance id is missing**")
        else:
            models.storage.reload()
            for i, obj in models.storage.all().items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    print(obj.__str__())
                    return
            print("**no instance found**")

    def do_destroy(self, args):
        """given an instance name and id, it will be eliminated"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            instances = models.storage.all()
            for i, obj in instances.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(instances[i])
                    models.storage.save()
                    return
            print("**no instance found**")

    def do_all(self, args):
        """prints the string representation of all instances"""
        args = shlex.split(args)
        if args ==[]:
            models.storage.reload()
             _list = []
            for i, obj in models.storage.all().items():
                 _list.append(obj.__str__())
             print(_list)
        elif args[0] not in classes:
                    print("**class doesn't exist**")
        else:
             models.storage.reload()
            _list = []
            for i, obj in models.storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    _list.append(obj.__str__())
            print(_list)

    def do_update(self, args):
        args = shlex.split(args)
        if args == []:
            print("**class name missing**")
        elif args[0] not in classes:
            print("**class doesn't exist**")
        elif len(args) == 1:
            print("**instance id missing**")
        else:
            models.storage.reload()
            instances = models.storage.all()
            for i, obj in instances.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    if len(args) == 2:
                        print("**attribute name missing**")
                        return
                    elif len(args) == 3:
                        print("**value missing**")
                        return
                    else:
                        narg = args[3]
                        if hasattr(obj, str(args[2])):
                            narg = (type(getattr(obj, args[2])))(args[3])
                        obj.__dict__[args[2]] = narg
                        models.storage.save()
                        return
            print("**no instance found**")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
