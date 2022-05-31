#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        message = ""
        if (i % 3 == 0) and (i % 5 == 0):
            message = "FizzBuzz"
        elif i % 3 == 0:
            message = "Fizz"
        elif i % 5 == 0:
            message = "Buzz"

        if message:
            print(message, end=" ")
        else:
            print(i, end=" ")
