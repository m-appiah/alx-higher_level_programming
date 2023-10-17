#!/usr/bin/python3
"""unittests for base.py"""

import unittest
import turtle
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def setUp(self):
        """Reset the counter before each test"""
        Base._Base__nb_objects = 0

    def test_instance_creation_with_id(self):
        """Test with id"""
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_instance_creation_without_id(self):
        """Test without id"""
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string_with_data(self):
        """Test to json string with data"""
        data = [{'id': 1, 'name': 'example'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "example"}]')

    def test_to_json_string_with_empty_data(self):
        """Test to json string with empty data"""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, '[]')

    def test_to_json_string_with_none(self):
        """Test to json string with None"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

    def test_save_to_file_with_data(self):
        """Save to file with data"""
        obj = Base()
        Base.save_to_file([obj])
        with open("Base.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[{"id": 1}]')
        os.remove("Base.json")

    def test_save_to_file_with_empty_data(self):
        """Save to file with empty data"""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[]')
        os.remove("Base.json")

    def test_save_to_file_with_none(self):
        """Save to file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            data = file.read()
        self.assertEqual(data, '[]')
        os.remove("Base.json")

    def test_from_json_string_with_data(self):
        """Test from json string with data"""
        json_str = '[{"id": 1, "name": "example"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{'id': 1, 'name': 'example'}])

    def test_from_json_string_with_empty_data(self):
        """Test from json string with empty data"""
        json_str = '[]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [])

    def test_from_json_string_with_none(self):
        """Test from json string with None"""
        json_str = None
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [])

    def test_create_with_rectangle(self):
        """Create with rectangle"""
        data = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        obj = Rectangle.create(**data)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_create_with_square(self):
        """Create with square"""
        data = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        obj = Square.create(**data)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_load_from_file_with_data(self):
        """Test load from file with data"""
        data = [{'id': 1, 'name': 'example'}]
        with open("Base.json", "w") as file:
            file.write(json.dumps(data))
        objects = Base.load_from_file()
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].id, 1)
        os.remove("Base.json")

    def test_load_from_file_with_empty_data(self):
        """Test load from file with empty data"""
        with open("Base.json", "w") as file:
            file.write("[]")
        objects = Base.load_from_file()
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 0)
        os.remove("Base.json")

    def test_load_from_file_with_none(self):
        """Test load from file with None"""
        objects = Base.load_from_file()
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 0)

    def test_save_to_file_csv_with_data(self):
        """Test save to file with csv data"""
        obj = Base()
        Base.save_to_file_csv([obj])
        with open("Base.csv", "r") as file:
            data = file.read()
        self.assertEqual(data.strip(), '1')
        os.remove("Base.csv")

    def test_save_to_file_csv_with_empty_data(self):
        """Test save to file csv with empty data"""
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            data = file.read()
        self.assertEqual(data.strip(), '')

    def test_load_from_file_csv_with_data(self):
        """Test load from file csv with data"""
        with open("Base.csv", "w") as file:
            file.write("1\n2\n3")
        objects = Base.load_from_file_csv()
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 3)
        self.assertEqual(objects[0].id, 1)
        os.remove("Base.csv")

    def test_load_from_file_csv_with_empty_data(self):
        """Test load from file csv with empty data"""
        with open("Base.csv", "w") as file:
            file.write("")
        objects = Base.load_from_file_csv()
        self.assertIsInstance(objects, list)
        self.assertEqual(len(objects), 0)

    def test_draw(self):
        """Test the draw method (visual test, manual verification)"""

        rect = Rectangle(50, 100, 10, 10)
        square = Square(50, 10, 10)
        Base.draw([rect], [square])

    def tearDown(self):
        """TearDown"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")


if __name__ == '__main__':
    unittest.main()
