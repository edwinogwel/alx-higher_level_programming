#!/usr/bin/python3
""" This module defines a locked class. """


class LockedClass:
    """
    Prevent the user from dynamically creating new
    instance attributes other than first_name.
    """
    __slots__ = ['first_name']
