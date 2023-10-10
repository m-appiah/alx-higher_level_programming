#!/usr/bin/python3

"""Add attributes for this Module"""


def add_attribute(obj, attr_name, attr_value):
    """Add attribute function that checks if an object can have attributes"""
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
                                    and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
