#!/usr/bin/python3
"""File Storage"""

import json
from os.path import isfile
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    """"serializes and deserializes json"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self, file__path=None):
        """"Constructor"""

        if file__path is not None:
            self.__file_path = file__path

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        JsObjs = {}
        for key, val in FileStorage.__objects.items():
            JsObjs[key] = val.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(JsObjs, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dict_objects = json.load(f)
                for key, val in dict_objects.items():
                    new_obj = eval(val["__class__"])(**val)
                    FileStorage.__objects[key] = new_obj
