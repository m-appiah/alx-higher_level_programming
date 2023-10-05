#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class definition for finding the max int using unittest"""
    def test_empty_list(self):
        """Test an empty list of integers"""
        empty = []
        self.assertIsNone(max_integer(empty), None)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_start(self):
        """Test maximun integer at the beginning of a list."""
        max_at_start = [4, 2, 1, 3]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_max_at_start(self):
        """Test a single element."""
        single_element = [4]
        self.assertEqual(max_integer(single_element), 4)

    def test_max_float(self):
        """Test float of a list."""
        max_float = [9.4, 7.2, 19.4, -3.2]
        self.assertEqual(max_integer(max_float), 19.4)

    def test_string(self):
        """Test a string."""
        test_strings = "Michael"
        self.assertEqual(max_integer(test_strings), 'i')

    def test_empty_string(self):
        """Test an empty string."""
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)


    if __name__ == '__main__':
        unittest.main()
