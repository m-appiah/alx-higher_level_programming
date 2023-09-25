#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in my_list:
            if counter == x:  # Check if the required number of integers has been printed
                break
            try:
                IntegerValue = int(i)
                print("{:d}".format(IntegerValue), end=' ')
                counter += 1
            except ValueError:
                continue
        print()
        return counter
    except TypeError:
        return counter
