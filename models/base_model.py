#!/usr/bin/python3
"""Module Base Model"""

from uuid import uuid4
from datetime import datetime
import models
from cmd import Cmd


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor init"""

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
        """Return: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__."""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict

    @classmethod
    def all(cls):
        """All instances of a class."""
        return "all " + cls.__name__

    @classmethod
    def count(cls):
        """Count instances of a class."""
        instances = models.storage.all()
        counter = 0
        for key, val in instances.items():
            if(val.__class__.__name__ == cls.__name__):
                counter += 1
        print(counter)
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
            for ins, obj in models.storage.all().items():
                if obj.__class__.__name__ == cls.__name__ and obj.id == id:
                    for key, value in attr.items():
                        new_arg = value
                        if hasattr(obj, key):
                            new_arg = (type(getattr(obj, key)))(value)
                        obj.__dict__[key] = new_arg
                        models.storage.save()
                    return "\n"
            return "update " + cls.__name__ + " " + id
        else:
            return "update " + cls.__name__ + " " + id + " " + attr + " " + val
