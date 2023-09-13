#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operators = ['+', '-', '*', '/']
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = 0
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        result = add(a, b)

    elif argv[2] == "-":
        result = sub(a, b)

    elif argv[2] == "*":
        result = mul(a, b)

    else:
        result = div(a, b)

    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, result))
