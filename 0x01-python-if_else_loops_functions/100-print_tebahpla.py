#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        j = 0
    else:
        j = 32

    print('{}'.format(chr(i - j)), end='')
