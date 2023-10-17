#!/usr/bin/python3
"""Base class for managing unique identifiers in other classes"""


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
