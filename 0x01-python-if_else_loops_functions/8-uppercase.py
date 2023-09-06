#!/usr/bin/python3

def uppercase(str):
    for i in str:
        num = ord(i)
        j = 0

        if num >= 97 and num <= 122:
            j = 32

        print("{}".format(chr(num - j)), end="")

    print()
