#!/usr/bin/python3
class Square:
    """  a square

    Attributes:
        __size (int): Size of square
        __position (int, int): Position offset to print, [0] horizontal, [1]
             vertical
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        """ current position setting """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ gets current area of square """
        return self.__size * self.__size

    def my_print(self):
        """ prints a square """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """ size of square """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
