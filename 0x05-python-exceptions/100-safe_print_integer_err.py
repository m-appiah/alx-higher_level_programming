#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=stderr)
        return False
