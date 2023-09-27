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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
