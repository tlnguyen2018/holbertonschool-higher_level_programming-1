#!/usr/bin/python3
""" Rectangle class module

"""


class Rectangle:
    """ A rectangle

    Attributes:
        __width (int)
        __height (int)
        __str (str): rectangle shown in string form (#)
        area (int)
        perimeter (int)
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        if self.height > 0 < self.width:
            for x in range(self.height):
                string += "#" * self.width
                if x != self.height - 1:
                    string += "\n"
        return string

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
