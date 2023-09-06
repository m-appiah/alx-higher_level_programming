#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    absolute_number = number * -1
else:
    absolute_number = number

last_digit = absolute_number % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
