#!/usr/bin/python3
"""Reads and prints the contents of a file."""


def read_file(filename=""):
    """
    Args:
        filename (str): The name of the file to read (optional).

    Returns:
        None
    """
    with open(filename, 'r') as file:
        for line in file:
            print(line, end="")
