#!/usr/bin/python3
""" This module defines a class 'Rectangle' """


class Rectangle:
    """ Definition of a rectangle by its width and height . """

    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the rectangle. """
        return self.height * self.width

    def perimeter(self):
        """ Return the perimeter of the rectangle. """
        if self.height and self.width:
            return 2 * (self.width + self.height)
        return 0
