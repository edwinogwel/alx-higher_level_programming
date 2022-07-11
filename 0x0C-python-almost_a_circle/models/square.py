""" This module defines a class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Definition of Square class """
    HEADERS = ('id', 'size', 'x', 'y')

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate a square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return a str rep. of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ Get size """
        return self.width

    @size.setter
    def size(self, size):
        """ Set size """
        self.width = size
        self.height = size
