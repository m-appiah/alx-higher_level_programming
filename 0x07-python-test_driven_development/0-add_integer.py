#!/usr/bin/python3
"""
Check if a and b are either integer or float
"""


def add_integer(a, b=98):
    """Cast a and b to integers if they are floats.
    Return the addition of a and b
    """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

if __name__=="__main__":
    import doctest
    doctest.testmod()
