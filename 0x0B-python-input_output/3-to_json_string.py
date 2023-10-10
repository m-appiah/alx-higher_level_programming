#!/usr/bin/python3
"""Module that Returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
