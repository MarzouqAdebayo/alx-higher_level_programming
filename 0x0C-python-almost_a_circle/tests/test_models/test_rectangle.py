#!/usr/bin/python3
""" Unittest for rectangle """
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ unittest for rectangle module """
    def test_module_docstring(self):
        """ Checks for module docstring """
        self.assertTrue(len(__import__("models").rectangle.__doc__) > 1)

    def test_class_docstring(self):
        """ Checks for class docstring """
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_function_docstring(self):
        """ Checks for function docstring """
        self.assertTrue(len(Rectangle.__init__.__doc__) > 1)

    def test_varying_args(self):
        """ Checks for varying args passed """
        self.assertEqual(Rectangle(3, 5).id, 4)
        self.assertEqual(Rectangle(3, 5, 7).id, 5)
        self.assertEqual(Rectangle(3, 5, 9, 2).id, 6)
        self.assertEqual(Rectangle(3, 5, 5, 6, 26).id, 26)
