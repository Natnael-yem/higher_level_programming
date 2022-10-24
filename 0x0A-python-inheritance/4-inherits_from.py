#!/usr/bin/python3
"""defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """checks if an object is inherited instance of a class.

    args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to.
    returns:
        if obj is an inherited instance of a_class - true or otherwise - false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
