#!/usr/bin/python3
"""Test Cases for rectangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        """Test if attributes are correctly initialized"""
        r = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 1)

    def test_area(self):
        """Test the area calculation"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test the display method"""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the string representation"""
        r = Rectangle(7, 7, 2, 3, 8)
        expected_str = "[Rectangle] (8) 2/3 - 7/7"
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        """Test the update method"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)
        r.update(3, 4, 5, 6, 7)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        r = Rectangle(3, 4, 1, 2, 5)
        expected_dict = {'id': 5, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_setters(self):
        """Test attribute setters"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.width = 10
        r.height = 20
        r.x = 5
        r.y = 5
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_invalid_values(self):
        """Test with invalid attribute values"""
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 5, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(5, 5, -1)


if __name__ == '__main__':
    unittest.main()
