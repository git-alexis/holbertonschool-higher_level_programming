#!/usr/bin/python3

""" is_same_class function """


def is_same_class(obj, a_class):
    """ return True if the object is exactly an instance of the specified class
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if obj is an instance of a_class, False otherwise
    """

    return type(obj) == a_class
