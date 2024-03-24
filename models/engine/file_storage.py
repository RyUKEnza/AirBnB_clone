import json
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

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

