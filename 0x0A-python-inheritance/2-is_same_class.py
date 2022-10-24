#!/usr/bin/python3
"""defines a class-checking function."""

def is_same_class(obj, a_class):
    """checkss if an object is exactly an instance of a given class

    args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to.
    returns:
        if obj is exactly an instance of a_class - true or otherwise - false
    """
    if type(obj) == a_class:
        return True
    return False
