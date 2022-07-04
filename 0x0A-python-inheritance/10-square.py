#!/usr/bin/python3
""" This module defines a class Square """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size):
        """ Instantiation with width """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise TypeError("size must be greater than 0")
        self.__size = size
