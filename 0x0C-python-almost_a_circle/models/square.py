#!/usr/bin/python3
from models.rectangle import Rectangle


""" Square module
"""


class Square(Rectangle):
    """ Square class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ square initializer, sends "size" to "height"
        and "width" in rectangle
        """
        self.validate("size", size)
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ square string
        """
        temp = super().__str__()
        return temp.rsplit('/', 1)[0]

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        """ sets both width and height to "size"
        """
        self.validate("size", size)
        self.__width = size
        self.__height = size

    @property
    def width(self):
        raise AttributeError("no attribute: width in Square")

    @property
    def height(self):
        raise AttributeError("no attribute: height in Square")

    @width.setter
    def width(self, width):
        raise AttributeError("no method: width in Square")

    @height.setter
    def height(self, height):
        raise AttributeError("no method: height in Square")

    def update(self, *args, **kwargs):
        """ square updater formats args and kwargs for rectangle update
        """
        fix = args
        if args and len(args) > 1:
            if args[1] is not None:
                self.validate("size", args[1])
            fix = list(args)
            fix.insert(1, fix[1])
            fix = tuple(fix)
        if kwargs and "size" in kwargs:
            self.size = kwargs.pop("size")
        super().update(*fix, **kwargs)

    def to_dictionary(self):
        """ square to dict
        """
        sqd = super().to_dictionary()
        del sqd["width"]
        del sqd["height"]
        return sqd