#!/usr/bin/python3
"""
Unittest for max_integer function
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger tests max integer function

    Args:
        unittest (_type_): _description_
    """

    def test_max_integer_empty_list(self):
        """Test max_integer with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        """Test max_integer with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_positive_numbers(self):
        """Test max_integer with a list containing positive numbers."""
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    def test_max_integer_negative_numbers(self):
        """Test max_integer with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)

    def test_max_integer_mixed_numbers(self):
        """Test max_integer with a list containing mixed positive and negative
        numbers."""
        self.assertEqual(max_integer([-1, 3, -2, 5, -4]), 5)

    def test_max_integer_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers."""
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_max_integer_large_list(self):
        """Test max_integer with a large list of numbers."""
        self.assertEqual(max_integer(list(range(10000))), 9999)


if __name__ == "__main__":
    unittest.main()
