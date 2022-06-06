#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return          # default value = None
    else:
        my_list.sort()
        largest = my_list.pop()
        return largest
