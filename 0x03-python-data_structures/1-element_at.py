#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrive an element from a list."""
    list_length = (len(my_list) - 1)
    if idx < 0:
        return None
    elif idx > list_length:
        return None
    else:
        return (my_list[idx])
