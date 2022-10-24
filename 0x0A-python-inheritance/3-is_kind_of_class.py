#!/usr/bin/python3
"""defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """checks if an object is instance or inherited instance of a class.

    args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to.
    returns:
        if obj is an instance and inherited instance of a_class - true or otherwise - false
    """
    if isinstance(obj, a_class):
        return True
    return False
