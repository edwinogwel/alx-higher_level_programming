#!/usr/bin/python3
""" Provides a function to work with files """


def write_file(filename="", text=""):
    """ Write to a file """
    with open(filename, "w") as file:
        return file.write(text)
