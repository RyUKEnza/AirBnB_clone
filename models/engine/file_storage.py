#!/usr/bin/python3
import json
import os
from os import path
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file_storage.json"
    __objects = {}

    def __init__(self):
        self.__file_path = "file_storage.json"

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = globals()[class_name](**value)
                    self.__objects[key] = obj_instance

    def remove_old_objects(self):
        max_objects = 10
        if len(self.__objects) > max_objects:
            keys_to_remove = list(self.__objects.keys())[:-max_objects]
            for key in keys_to_remove:
                del self.__objects[key]

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
        else:
            print("Object not found")
