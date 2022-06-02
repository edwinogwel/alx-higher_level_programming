#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv)
    if args == 1:
        print(f"{args - 1} arguments.")
    elif args == 2:
        print(f"{args - 1} argument:")
    else:
        print(f"{args - 1} arguments:")

    for i in range(1, args):
        print(f"{i}: {argv[i]}")
