#!/usr/bin/python3

""" BaseGeometry class """


class BaseGeometry:

    """ Empty __init__ method class """

    def area(self):
        """ Raises an Exception with the message: area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value if it's an integer > 0 """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
