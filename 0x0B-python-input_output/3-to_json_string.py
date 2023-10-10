#!/usr/bin/python3
import json
"""Module that Returns the JSON representation of an object as a string"""


def to_json_string(my_obj):
    """
    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
