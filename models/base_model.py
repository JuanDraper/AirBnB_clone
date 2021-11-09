#!/usr/bin/python3
""" Base Model"""

from uuid import uuid4
from datetime import datetime
import models
from cmd import Cmd

class BaseModel:
    """ class"""

    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs is not None and kwargs != {}:
            for i in kwargs.keys():
                self.__dict__[i] = kwargs[i]
                if i == 'created_at' or i == 'updated_at':
                    dateFormat = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[i] = datetime.strptime(kwargs[i], dateFormat)
                    return
 
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)
    def __str__(self):
        """ returns the printable of [ class name], (self.id) and self.__dict"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary with kew/value of dict"""
        newDict = self.__dict__.copy()
        newDict["__Class__"] = self.__class__.__name__
        newDict["created_at"] = newDict["created_at"].isoformat()
        newDict["updated_at"] = newDict["updated_at"].isoformat()
        return newDict

    
