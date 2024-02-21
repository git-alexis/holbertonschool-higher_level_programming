#!/usr/bin/python3

""" Base class """


class Base:

    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the base class with an id.
        If id is None, it will increment the __nb_objects class variable.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
