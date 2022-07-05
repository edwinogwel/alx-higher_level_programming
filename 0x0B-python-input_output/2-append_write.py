#!/usr/bin/python3
""" Provides a function to work with files """


def append_write(filename="", text=""):
    """ Append text to a file """
    with open(filename, "a") as file:
        return file.write(text)
