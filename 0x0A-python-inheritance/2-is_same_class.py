#!/usr/bin/python3
""" Check if an obj is of a certain cls """


def is_same_class(obj, a_class):
    """ Return True if obj belongs to cls else False """
    return type(obj) == a_class
