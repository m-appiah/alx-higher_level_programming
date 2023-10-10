#!/usr/bin/python3
"""Inherited class"""


class MyList(list):
    """implementation of sorted list"""
    def print_sorted(self):
        """print sorted list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
