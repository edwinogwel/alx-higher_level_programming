#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    last_index = len(my_list) - 1       # indexing starts at 0(zero)
    copy = my_list.copy()

    if idx < 0 or idx > last_index:
        return copy
    else:
        copy[idx] = element
        return copy
