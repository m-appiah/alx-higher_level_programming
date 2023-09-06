#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        char = chr(i)
    else:
        char = chr(i - 32)

    print(char, end='')
