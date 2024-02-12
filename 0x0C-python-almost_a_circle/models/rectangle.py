#!/usr/bin/python3
""" Contains the Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle _summary_

    Args:
        Base (class): inherited parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ _summary_

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter for width private attribute

        Returns:
            int: the width of the rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width the width of the rectangle instance

        Args:
            value (int): the value of the width

        Raises:
            TypeError: when width is not of type int
            ValueError: when width is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter for height private attribute

        Returns:
            int: the height of the rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height the height of the rectangle instance

        Args:
            value (int): the value of the height

        Raises:
            TypeError: when height is not of type int
            ValueError: when height is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x - getter for x attribute

        Returns:
            int: x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x - setter for x attribute

        Args:
            value (int): value for x

        Raises:
            TypeError: when x is not of type int
            ValueError: when x is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y - getter for y attribute

        Returns:
            int: y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y - setter for x attribute

        Args:
            value (int): value for y

        Raises:
            TypeError: when y is not of type int
            ValueError: when y is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area - computes and returns the area of the
        rectangle instance

        Returns:
            int: area of the rectangle instance
        """
        return self.height * self.width

    def display(self):
        """display prints a user friendly string

        Returns:
            _type_: _description_
        """
        for _ in range(0, self.y):
            print()
        for _ in range(0, self.height):
            for _ in range(0, self.x):
                print(end=" ")
            for _ in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ prints a user friendly string

        Returns:
            str: information about the Rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update updates the instance using args and kwargs
        """
        attrs = ['id', 'width', 'height', 'x', 'y']

        if args is not None and len(args) != 0:
            for i, item in enumerate(args):
                setattr(self, attrs[i], item)
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary returns the dictionary rep of the instance

        Returns:
            dict: the dictionary representation of the instance
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        attrs_dict = {}
        for key in attrs:
            if key == "id":
                attrs_dict[key] = (self.__dict__)[key]
            else:
                attrs_dict[key] = (self.__dict__)["_Rectangle__" + key]
        return attrs_dict
