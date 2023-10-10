#!/usr/bin/python3
"""Reads and prints the contents of a file."""


def read_file(filename=""):
    """
    Args:
        filename (str): The name of the file to read (optional).

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
