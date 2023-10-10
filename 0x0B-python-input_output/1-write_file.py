#!/usr/bin/python3
"""Writes a string to a text file (UTF-8) and returns num chars"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
