#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_of_int = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            num_of_int += 1
        except (ValueError, TypeError):
            pass
    print()
    return (num_of_int)
