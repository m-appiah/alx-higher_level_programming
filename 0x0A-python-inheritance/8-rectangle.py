#!/usr/bin/python3
"""raising an exception for umimplemented class method """


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """area function or method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the "value" argument.
        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherit the base geometry"""

    def __init__(self, width, height):
        """Method or function instantiation

        Args:
            name (str): The name of the value.
            value (int): The value to validate."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
