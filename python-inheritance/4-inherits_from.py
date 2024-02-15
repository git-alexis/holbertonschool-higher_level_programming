#!/usr/bin/python3

""" inherits_from function """


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if obj is an instance of a class that inherited from a_class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
