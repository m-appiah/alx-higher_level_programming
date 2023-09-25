#!/usr/bin/python3
def safe_print_integer(value):
    try:
        '''print("{:d}".format(value))'''
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except(ValueError, TypeError):
        return False
