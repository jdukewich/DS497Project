"""
pip install python-constraint
pip install numpy
"""
from constraint import *
import numpy as np
<<<<<<< HEAD


def test():
    problem = Problem()
    for i in range(81):
        problem.addVariable(i, [1,2,3,4,5,6,7,8,9])

	rows = np.array([i for i in range(0,9)])
	cols = np.array([j for j in range(0,81,9)])
	
	# Add 27 AllDif constraints, one for each row, column, and box
	for i in range(9):
		add = np.ones(9, np.int8)*i*9
		constr = (rows+add).tolist()
		problem.addConstraint(AllDifferentConstraint(), constr)

	for i in range(9):
		add = np.ones(9, np.int8)*i
		constr = (cols+add).tolist()
		problem.addConstraint(AllDifferentConstraint(), constr)

	for i in range(0, 7, 3):
		box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
		problem.addConstraint(AllDifferentConstraint(), box)

	for i in range(27, 34, 3):
		box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
		problem.addConstraint(AllDifferentConstraint(), box)

	for i in range(54, 61, 3):
		box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
		problem.addConstraint(AllDifferentConstraint(), box)
	answer = problem.getSolution()
	return answer


def make_board_from_dict(board):
	new_board = [[board[i+9*j] for i in range(9)] for j in range(9)]
  	return new_board
