#!/usr/bin/python3
from models.base_model import BaseModel
import json
from os.path import isfile


class FileStorage:
    """Serializes instances to JSON file, and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        class_obj_name = obj.__class__.__name__
        key = "{}.{}".format(class_obj_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file."""
        serial_obj = {}
        all_objcts = FileStorage.__objects
        for objct in all_objcts.keys():
            serial_obj[objct] = all_objcts[objct].to_dict()
            
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    de_obj = json.load(file)
                    for key, val in de_obj.items():
                        class_name = key.split('.')[0]
                        obj_id = key.split('.')[1]
                        
                        my_class = eval(class_name)
                        obj_instance = my_class(**val)
                        FileStorage.__objects[key] = obj_instance
                except Exception:
                    pass
