#!/usr/bin/python3

import sys
import unittest
from unittest.mock import Mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import tkinter as TK
import turtle
from models.base import Base


"""Test cases for the square module"""


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        """Test valid input"""
        square1 = Square(5, 2, 3, 1)
        self.assertEqual(square1.size, 5)
        self.assertEqual(square1.x, 2)
        self.assertEqual(square1.y, 3)
        self.assertEqual(square1.id, 1)

        """Test invalid input (e.g., negative size)"""
        with self.assertRaises(ValueError):
            Square(-1, 2, 3, 1)

        """Test invalid input (e.g., non-integer values)"""
        with self.assertRaises(TypeError):
            Square("not an int", 2, 3, 1)

    def test_string_representation(self):
        square = Square(4, 0, 0, 1)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 4")

    def test_update(self):
        square = Square(4, 0, 0, 1)

        """Test update with positional arguments"""
        square.update(2)
        self.assertEqual(square.id, 2)

        square.update(3, 5, 6, 7)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

        """Test update with invalid arguments"""
        with self.assertRaises(TypeError):
            square.update("invalid")

    def test_to_dictionary(self):
        square = Square(4, 0, 0, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 4, 'x': 0, 'y': 0}
        self.assertEqual(square_dict, expected_dict)

    def test_negative_position(self):
        """Test square with a negative position"""
        square = Square(4, -2, -3, 1)
        self.assertEqual(square.x, -2)
        self.assertEqual(square.y, -3)

    def test_update_with_kwargs(self):
        """Test update method with keyword arguments"""
        square = Square(4, 0, 0, 1)
        square.update(size=3, x=2, y=2)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)


if __name__ == '__main__':
    unittest.main()
