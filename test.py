"""
pip install python-constraint
pip install numpy
"""
from constraint import *
import numpy as np
import math


def test(board):
    """
    Return an N by N array that is the solution to the N by N input board

    Uses the python-constraint CSP library. The library solution comes out as a
    dictionary, but I convert it to an N by N array in the last step
    """
    size = len(board)
    sqrt_size = int(math.sqrt(size))
    problem = Problem()

    # Iterate through the input board and add each element as a variable
    # The domain will be just the value if it's given, or [1, ..., size] otherwise
    for i in range(size**2):
        if board[i//size][i % size] == 0:
            problem.addVariable(i, [i for i in range(1, size+1)])
        else:
            problem.addVariable(i, [board[i//size][i % size]])

    rows = np.array([i for i in range(size)])
    cols = np.array([j for j in range(0, size**2, size)])

    # Create size # of AllDiff constraints for each row
    for i in range(size):
        add = np.ones(size, np.int8)*i*size
        constr = (rows+add).tolist()
        problem.addConstraint(AllDifferentConstraint(), constr)

    # Create size # of AllDiff constraints for each column
    for i in range(size):
        add = np.ones(size, np.int8)*i
        constr = (cols+add).tolist()
        problem.addConstraint(AllDifferentConstraint(), constr)

    # Create size # of AllDiff constraints for each box
    for i in range(sqrt_size):
        for j in range(sqrt_size):
            box = []
            # The top left entry of each box, will be 0, 3, 6, 26, 30, 33, etc for a 9 x 9
            top_left = size*sqrt_size*i + sqrt_size*j
            for k in range(sqrt_size):
                box.extend((top_left+k*size, top_left+k*size+1, top_left+k*size+2))
            problem.addConstraint(AllDifferentConstraint(), box)

    answer = problem.getSolution()

    # Make an array from the solution dictionary
    new_board = [[answer[i+size*j] for i in range(size)] for j in range(size)]
    return new_board

