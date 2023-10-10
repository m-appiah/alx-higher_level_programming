#!/usr/bin/python3
"""raising an exception for umimplemented class method """


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """area function or method that is not implemented"""
        raise Exception("area() is not implemented")
