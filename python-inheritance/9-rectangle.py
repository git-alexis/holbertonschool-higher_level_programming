#!/usr/bin/python3

""" Rectangle class that inherits from BaseGeometry class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ Class that defines a Rectangle with BaseGeometry inheritance """

    def __init__(self, width, height):
        """
        Initialise the class with instance attribute height and width
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
