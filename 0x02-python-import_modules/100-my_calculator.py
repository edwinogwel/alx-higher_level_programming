#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    nArgs = len(argv)
    if nArgs != 4:      # argv[0] -> program name
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])    # 1st arg
    op = argv[2]        # operator
    b = int(argv[3])    # 2nd arg

    message = ""
    if op == '+':
        message = f"{a} {op} {b} = {add(a, b)}"
    if op == '-':
        message = f"{a} {op} {b} = {sub(a, b)}"
    if op == '*':
        message = f"{a} {op} {b} = {mul(a, b)}"
    if op == '/':
        message = f"{a} {op} {b} = {div(a, b)}"

    print(message) if message else print(
        "Unknown operator. Available operators: +, -, * and /") & exit(1)