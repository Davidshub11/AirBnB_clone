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
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = Filestrorage.__objects
        obj_dict = {}

        for key, val in all_objs.items():
            obj_dict[key] = val.to_dict()

        with open(FileStrorage.__file_path, "w", encoding="utf-8") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isFile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                try:
                    obj_dict = json.load(fd)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)

                        FileStrorage.__objects[key] = instance
                except Exeception:
                    pass
