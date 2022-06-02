#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:      # argv[0] -> program name
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {op} {b} = {ops[op](a, b)}")
