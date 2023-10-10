#!/usr/bin/python3
"""Function that returns True if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True or otherwise False
    """
    return isinstance(obj, a_class)
