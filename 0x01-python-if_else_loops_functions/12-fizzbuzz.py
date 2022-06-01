#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        message = ""
        if i % 15 == 0:
            message = "FizzBuzz"
        elif i % 3 == 0:
            message = "Fizz"
        elif i % 5 == 0:
            message = "Buzz"
        print(message, end=" ") if message else print(i, end=" ")
