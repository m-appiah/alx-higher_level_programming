#!/usr/bin/python3
"""A Square class that will be used to instantiate an object"""


class Square:
    """An ampty class Square that defines a square.
    At the moment, it has no attributes or properties.
    """

    def __init__(self, size=0):
        """Initialization method of the class
                Args:
                        size (int): Size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square instance
                Returns:
                        Integer: Square of the size
                """
        return (self.__size ** 2)
