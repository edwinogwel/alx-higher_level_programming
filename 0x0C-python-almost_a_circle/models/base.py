""" Provides a Base class for other classes """


class Base:
    """ Definition of Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiate a base object """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
