#!/usr/bin/python3

""" Rectangle class """


from models.base import Base


class Rectangle(Base):

    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class with an id,
        width, height, x, and y attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Returns the x value of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x value of the rectangle """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns the y value of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y value of the rectangle """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle with the character # """
        for blanck_line in range(self.__y):
            print()
        for line in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="")
            print()

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the rectangle """
        if args:
            attributs = ["id", "width", "height", "x", "y"]
            for index in range(len(args)):
                setattr(self, attributs[index], args[index])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
