#!/usr/bin/python3
"""Base class for managing unique identifiers in other classes"""
import json


class Base:
    """
    The Base class for managing unique identifiers in other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a json file"""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dict)
        with open(filename, "w") as file:
            file.write(json_str)
