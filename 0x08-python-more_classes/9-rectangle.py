#!/usr/bin/python3
""" This module defines a class 'Rectangle' """


class Rectangle:
    """ Definition of a rectangle by its width and height . """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle. """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Return a representation of a rectangle with '#' char. """
        if self.height and self.width:
            return '\n'.join([str(self.print_symbol) * self.width] * self.height)
        return ""

    def __repr__(self):
        """ Return a string representation of the rectangle to be
            able to recreate a new instance by using eval(). """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Delete a rectangle. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the rectangle. """
        if self.height and self.width:
            return 2 * (self.width + self.height)
        return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the rectangle with the biggest area. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance or Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance or Rectangle")
        if rect_2.area() >= rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Return a new rectangle with width == height == size. """
        return cls(size, size)
