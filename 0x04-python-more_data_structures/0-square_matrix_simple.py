#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    if matrix is None:
        return None
    return ([list(map(lambda x: x * x, row)) for row in matrix])
