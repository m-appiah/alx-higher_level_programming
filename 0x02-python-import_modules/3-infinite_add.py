#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    arguments = argv[1:]

    result = 0
    for arg in arguments:
        result = result + int(arg)

    print(result)
