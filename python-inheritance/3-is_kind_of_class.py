#!/usr/bin/python3

""" is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ return True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if obj is an instance of a_class, False otherwise
    """

    return isinstance(obj, a_class)
