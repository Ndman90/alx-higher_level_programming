#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modify"""

    list_length = len(my_list)
    new_list = my_list
    if idx < 0:
        return my_list
    elif idx > list_length:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
