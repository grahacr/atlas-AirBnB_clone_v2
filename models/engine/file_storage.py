#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        # If it's none, return all
        if cls is None:
            return FileStorage.__objects
        else:
            # Else, create a temp dictionary.
            temp_dict = {}
            # Loop through all objects
            for key, value in FileStorage.__objects.items():
                # IF current object loop matches the object passed,
                # Add to the temp dictionary
                if value.__class__ is cls:
                    temp_dict[key] = value
            # Return the recently created dictionary.
            return temp_dict
        """Returns a dictionary of models currently in storage"""

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ Deletes the specified object, if none is pass, do nothing"""
        if obj is None:
            return
        else:
            # Get the class name, and the ID as a key value.
            keyvalue = type(obj).__name__ + "." + obj.id
            # Check if it exists.
            if keyvalue in FileStorage.__objects:
                # If it does, delete it.
                del FileStorage.__objects[keyvalue]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
