#!/usr/bin/python3
"""Function to check if an object is exactly an instance of a given class"""


def is_same_class(obj, a_class):
    """
    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Return:
        bool: True or False otherwis
        """
    return type(obj) == a_class
