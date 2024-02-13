#!/usr/bin/python3
""" The 'base' module - contains the base class"""


import json
import csv


class Base:
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilaizes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string

        Args:
            list: any

        Returns:
            str: json serialized string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Args:
            list_objs (list): list of class object instances
        """
        filename = cls.__name__ + ".json"
        data = []

        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Args:
            json_string (string): the json string

        Returns:
            object: json loaded data
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create

        Returns:
            class: class instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file loads and creates instances from file

        Returns:
            list: list of the created instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
                inst_arr = []
                for inst in data:
                    inst_arr.append(cls.create(**inst))
                return inst_arr
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file save to csv file

        Args:
            list_objs (list): list of class object instances
        """
        filename = cls.__name__ + ".csv"
        data = []

        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())

        with open(filename, mode="w", encoding="utf-8") as f:
            field_name = []
            if cls.__name__ == 'Rectangle':
                field_name = ["id", "width", "height", "x", "y"]
            if cls.__name__ == 'Square':
                field_name = ["id", "size", "x", "y"]
            w = csv.DictWriter(f, fieldnames=field_name)
            w.writeheader()
            w.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file loads from csv and creates instances from file

        Returns:
            list: list of the created instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                data = csv.DictReader(f)
                x = [{key: int(value) for key, value in row.items()} for
                     row in data]
                inst_arr = []
                for inst in x:
                    inst_arr.append(cls.create(**inst))
                return inst_arr
        except Exception:
            return []
