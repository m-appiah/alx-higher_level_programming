#!/usr/bin/python3
"""Base class for managing unique identifiers in other classes"""
import json
import csv
import turtle
import os


class Base:
    """
    The Base class for managing unique identifiers in other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a json file"""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dict)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Load a list of dictionaries from a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_str = file.read()
            list_dict = cls.from_json_string(json_str)
            return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csvwriter.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as csvfile:
                csvreader = csv.reader(csvfile)
                instances = []
                for row in csvreader:
                    row = [int(val) for val in row]
                    if cls.__name__ == "Rectangle":
                        instance = cls(1, 1)
                        (
                                instance.id,
                                instance.width,
                                instance.height,
                                instance.x,
                                instance.y
                                ) = row

                    elif cls.__name__ == "Square":
                        instance = cls(1)
                        (
                                instance.id,
                                instance.size,
                                instance.x,
                                instance.y
                                ) = row
                        instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Create a Turtle screen and set up options"""
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        """Create a Turtle object for drawing"""
        drawer = turtle.Turtle()
        drawer.speed(1)

        def draw_rectangle(rectangle):
            """draw a rectangle"""
            for _ in range(2):
                drawer.forward(rectangle.width)
                drawer.left(90)
                drawer.forward(rectangle.height)
                drawer.left(90)

        def draw_square(square):
            """draw a square"""
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)

        """Draw the rectangles"""
        for rectangle in list_rectangles:
            drawer.penup()
            drawer.goto(rectangle.x, rectangle.y)
            drawer.pendown()
            draw_rectangle(rectangle)

        """Draw the squares"""
        for square in list_squares:
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            draw_square(square)

        """Close the drawing window on click"""
        screen.exitonclick()
