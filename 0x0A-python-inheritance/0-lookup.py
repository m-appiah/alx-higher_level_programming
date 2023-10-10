#!/usr/bin/python3

""" Function that chcks for attribute and metthods of an object"""


def lookup(obj):
    """
    Returns available attributes and methods of an object.
    Args:
        obj - object to be checked
    Return: list
    """
    return(dir(obj))
