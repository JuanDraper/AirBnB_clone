#!/usr/bin/python3
"""Base Model"""

from uuid import uuid4
from datetime import datetime
import models
from cmd import Cmd


class BaseModel:
    """Class"""

    def __init__(self, *args, **kwargs):
        """ init"""

        if kwargs is not None and kwargs != {}:
            for k in kwargs.keys():
                self.__dict__[k] = kwargs[k]
                if k == 'created_at' or k == 'updated_at':
                    d_format = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[k] = datetime.strptime(kwargs[k], d_format)
            return

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """returns the printable of [class name].(self.id) and self_dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """dictionary with kew/value of dict"""

        newDict = self.__dict__.copy()
        newDict["__class__"] = self.__class__.__name__
        newDict["created_at"] = new_dict["created_at"].isoformat()
        newDict["updated_at"] = new_dict["updated_at"].isoformat()
        return newDict

    @classmethod
    def all(cls):
        """All instances of a class."""
        return "all " + cls.__name__

    @classmethod
    def count(cls):
        """Count instances of a class."""
        instances = models.storage.all()
        c = 0
        for k, v in instances.items():
            if(v.__class__.__name__ == cls.__name__):
                c += 1
        print(c)
        return "\n"

    @classmethod
    def show(cls, id=""):
        """Shows a given instance by id."""
        return "show " + cls.__name__ + " " + id

    @classmethod
    def destroy(cls, id=""):
        """Deletes an instance of a class."""
        return "destroy " + cls.__name__ + " " + id

    @classmethod
    def update(cls, id="", attr="", val=""):
        """Updates an instance of a class."""
        if id != "" and type(attr) is dict:
            for i, obj in models.storage.all().items():
                if obj.__class__.__name__ == cls.__name__ and obj.id == id:
                    for k, v in attr.items():
                        new_arg = v
                        if hasattr(obj, k):
                            new_arg = (type(getattr(obj, k)))(v)
                        obj.__dict__[k] = new_arg
                        models.storage.save()
                    return "\n"
            return "update " + cls.__name__ + " " + id
        else:
            return "update " + cls.__name__ + " " + id + " " + attr + " " + val
