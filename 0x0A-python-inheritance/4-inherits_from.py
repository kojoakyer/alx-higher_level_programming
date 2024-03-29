#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class match the type of obj to.
    Returns:
        If obj an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
