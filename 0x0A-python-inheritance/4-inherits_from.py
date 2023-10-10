#!/usr/bin/python3
"""Returns True if the object is an instance of a class or otherwise False."""


def inherits_from(obj, a_class):
    """
    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True or False otherwise
    """
    return issubclass(type(obj), a_class)
