#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ Invert the equality magic methods"""
    def __eq__(self, other):
        """"""
        return other.__ne__(self)

    def __ne__(self, other):
        """ Invert the equality magic methods"""
        return other.__eq__(self)
