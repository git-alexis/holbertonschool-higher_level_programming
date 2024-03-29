#!/usr/bin/python3

""" lookup function """


def lookup(obj):
    """ Returns list of available attributes and methods of an object
    Args:
        obj: object to look up
    Returns:
        list of attributes and methods
     """

    return dir(obj)
