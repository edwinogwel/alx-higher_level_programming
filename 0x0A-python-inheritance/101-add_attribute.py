#!/usr/bin/python3
"""
This module provides a function to add
an attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """ Add an attribute to an object """
    if getattr(obj, "__dict__", None) is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
