#!/usr/bin/python3

""" Square class that inherits from Rectangle class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ Class that defines a Square with Rectangle inheritance """

    def __init__(self, size):
        """
        Initialise the class with instance attribute size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ Returns the string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)
