from models.base import Base


class Rectangle(Base):
    """ Definition of Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiate a rectangle object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


@property
def width(self):
    """ Get width """
    return self.__width


@width.setter
def width(self, value):
    """ Set width """
    self.__width = value


@property
def height(self):
    """ Get height """
    return self.__height


@height.setter
def height(self, value):
    """ Set height """
    self.__height = value


@property
def x(self):
    """ Get x """
    return self.__x


@x.setter
def x(self, value):
    """ Set x """
    self.__x = value


@property
def y(self):
    """ Get y """
    return self.__y


@y.setter
def y(self, value):
    """ Set y """
    self.__y = value
