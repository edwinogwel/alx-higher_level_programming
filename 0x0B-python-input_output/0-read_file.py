#!/usr/bin/python3
""" Provides a function to work with files """


def read_file(filename=""):
    """ Read file content and print it """
    with open(filename) as file:
        read_data = file.read()
        print(read_data, end="")
