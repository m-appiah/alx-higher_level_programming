#!/usr/bin/python3
"""A Square class that will be used to instantiate an object"""


class Square:
    """An ampty class Square that defines a square.
    At the moment, it has no attributes or properties.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method of the class
                Args:
                        size (int): Size of the square
        """
        self.size = size #setter property
        self.position = position #setter property

    @property
    def size(self):
        """Retrieve the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Get/set the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square instance
                Returns:
                        Integer: Square of the size
                """
        return (self.__size ** 2)
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
            return

       for _ in range(self.__position[1]):
           print()
       for _ in range(self.__size):
           print(" " * self.__position[0] + "#" * self.__size)
