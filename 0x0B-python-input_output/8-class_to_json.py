#!/usr/bin/python3
"""This module defines a Python for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
