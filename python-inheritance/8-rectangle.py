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
