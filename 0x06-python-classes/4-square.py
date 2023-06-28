#!/usr/bin/python3
"""Define a square."""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            size (int): size of the square
        """
        self.__size = size
    @property
    def size(self):
        """Gt/set value of size"""
        return self.__size

    @size.setter
    def size(self, value)
        """Setter mettod for value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)
