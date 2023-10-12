#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    if set_1 is None or set_2 is None:
        return None
    return (set_1 ^ set_2)
