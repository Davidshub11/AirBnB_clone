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
        key = "{}.{}".format(obj_cls_name, obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists,
        otherwise nothing happens.
        """
        try:
            if not os.path.exists(self.__file_path):
                return  # Return early if the file does not exist

            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

                for key, value in obj_dict.items():
                    cls_name = value.get("__class__")
                    if cls_name:
                        cls = models.classes.get(cls_name)
                        if cls:
                            self.new(cls(**value))
                    else:
                        print("Missing class name in JSON data.")

        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data.")
        except Exception as e:
            print(f"An error occurred: {e}")
