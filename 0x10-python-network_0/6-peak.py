#!/usr/bin/python3
""" Finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    if not list_of_integers:
        return None

    lower, higher = 0, len(list_of_integers) - 1

    while lower < higher:
        middle = (lower + higher) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1]:
            higher = middle
        else:
            lower = middle + 1

    return list_of_integers[lower]
