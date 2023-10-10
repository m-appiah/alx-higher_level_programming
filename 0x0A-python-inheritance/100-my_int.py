#!/usr/bin/python3
"""Class for the MYInt"""


class MyInt(int):
    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if not equal, False if they are equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if equal, False if they are not equal.
        """
        return super().__eq__(other)
