#!/usr/bin/pyton3
""" Square module contains the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition

    Args:
        Rectangle (class): Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ _summary_

        Args:
            size (int): size of square
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ prints a user friendly string

        Returns:
            str: information about the Square instance
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """size - getter for size

        Returns:
            int: size of the square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """size - setter for size

        Raises:
            TypeError: when value is not of type int
            ValueError: when value is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update updates the instance using args and kwargs
        """
        attrs = ['id', 'size', 'x', 'y']

        if args is not None and len(args) != 0:
            for i, item in enumerate(args):
                setattr(self, attrs[i], item)
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attrs:
                    if key == "size":
                        setattr(self, 'width', value)
                        setattr(self, 'height', value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary returns the dictionary rep of the instance

        Returns:
            dict: the dictionary representation of the instance
        """
        attrs = ['id', 'size', 'x', 'y']
        attrs_dict = {}
        for key in attrs:
            if key == "id":
                attrs_dict[key] = (self.__dict__)[key]
            elif key == "size":
                attrs_dict[key] = (self.__dict__)["_Rectangle__" + "width"]
            else:
                attrs_dict[key] = (self.__dict__)["_Rectangle__" + key]
        return attrs_dict
