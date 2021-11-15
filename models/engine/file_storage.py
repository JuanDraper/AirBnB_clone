#!/usr/bin/python3
""" File Storage"""

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
    """"Class """

    __file_path = "file.json"
    __objects = {}

    def __init__(self, file__path=None):
        """constructor"""

        if file__path is not None:
            FileStorage.__file_path = file__path

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def all(self):
        """"returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        jso = {}
        for key, val in FileStorage.__objects.items():
            jso[key] = val.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(jso, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                dic = json.load(f)
                for k, v in dic.items():
                    nObj = eval(v["__class__"])(**v)
                    FileStorage.__objects[k] = nObj
