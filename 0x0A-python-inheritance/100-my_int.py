#!/usr/bin/python3

"""Class for the MyInt"""


class MyInt(int):
    """A New Int that rebels"""

    def __eq__(self, other):
        # Override == (equality) to behave as !=
        return super().__ne__(other)

    def __ne__(self, other):
        # Override != (inequality) to behave as ==
        return super().__eq__(other)
