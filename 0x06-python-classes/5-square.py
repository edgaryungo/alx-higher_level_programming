#!/usr/bin/python3
"""Define a square."""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get/set current value of size"""
        return self.__size

    @size.setter
    def size(self, value)
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
