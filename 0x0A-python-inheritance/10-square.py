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
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    def __init__(self, size):
        """Instatiation of a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
