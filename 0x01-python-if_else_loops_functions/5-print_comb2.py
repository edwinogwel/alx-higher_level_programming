#!/usr/bin/python3
for number in range(100):
    if number == 99:
        print(number)
    else:
        print(f"{number:0>2d}", end=", ")
