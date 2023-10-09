#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    list_length = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > list_length:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list[idx])
