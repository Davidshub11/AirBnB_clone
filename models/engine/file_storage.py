#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Arguments:
                obj : An instance object.
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        from models.base_model import BaseModel
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                        cls_name, obj_id = key.split('.')
                        obj = BaseModel(value)
                        self.new(obj)

        except FileNotFoundError:
            pass
