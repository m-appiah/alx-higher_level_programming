#!/usr/bin/python3
def print_last_digit(number):
    ab = number / 10
    del ab
    digit = int(str(number)[-1])
    print(digit, end="")
    return digit
