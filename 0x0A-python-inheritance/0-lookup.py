#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object for which to retrieve attributes and methods.

    Returns:
        list: Containing the names of the available attributes and methods
    """
    return(dir(obj))
