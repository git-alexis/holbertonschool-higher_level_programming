#!/usr/bin/python3

"""class that defines a Square"""


class Square:

    """Initialise the class with a private instance attribute size"""

    def __init__(self, size=0):
        """Check execption tupe and value for size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
