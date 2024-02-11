#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:

    """class that defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise the class with a private instance attribute width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Check execption type and value for width and set the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Check execption type and value for height and set the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle"""
        rectangle_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for line in range(self.__height):
            for index in range(self.__width):
                rectangle_string += str(self.print_symbol)
            rectangle_string += "\n"

        return rectangle_string[:-1]

    def __repr__(self):
        """Return the printable representation of Rectangle object"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
