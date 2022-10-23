#!/usr/bin/python3
"""Defines a rectangle class """

class Rectangle:
    """Represent a class rectangle"""
    __width = None
    __height = None

    def __int__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
           self.__height = value
