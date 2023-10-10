#!/usr/bin/python3
"""Appends a string and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to append to (optional).
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
