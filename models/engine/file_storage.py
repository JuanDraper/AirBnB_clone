import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City":
           City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """serializes and deserializes json"""

    __file_path = "file.json"
    __objects = {}

    def init(self, file__path=None):
        """constructor"""
        if file__path is not None:
            self.__file_path = file__path

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        jso = {}
        for k, v in self.__objects.items():
            jso[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(jso, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                dic = json.loads(f.read())
                for k, v in dic.items():
                    cls = k.split('.')[0]
                    if cls in classes:
                        self._objects[k] = classes[cls](**v)
        except Exception:
            pass
