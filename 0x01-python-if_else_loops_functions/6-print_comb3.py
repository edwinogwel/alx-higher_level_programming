#!/usr/bin/python3
for number in range(9):
    for another in range(number + 1, 10):
        if number == 8:
            print("{}{}".format(number, another))
        else:
            print("{}{}".format(number, another), end=", ")
