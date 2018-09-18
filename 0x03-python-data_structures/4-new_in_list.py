#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    if 0 <= idx < len(my_list):
        new = my_list[:]
        new[idx] = element
        return new
    else:
        return None
