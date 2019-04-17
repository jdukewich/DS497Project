"""
pip install python-constraint
"""
from constraint import *

def test():
	problem = Problem()
	for i in range(81):
	    problem.addVariable(i, [1,2,3,4,5,6,7,8,9])

	rows = [i for i in range(0,81,9)]
	cols = [j for j in range(9)]
	# Add 27 AllDif constraints, one for each row, column, and box
	for i in range(9):
	    problem.addConstraint(AllDifferentConstraint(), rows)

	for i in range(9):
	    problem.addConstraint(AllDifferentConstraint(), cols)

	for i in range(0, 7, 3):
	    box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
	    problem.addConstraint(AllDifferentConstraint(), box)

	for i in range(27, 34, 3):
	    box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
	    problem.addConstraint(AllDifferentConstraint(), box)

	for i in range(54, 61, 3):
	    box = [i, i+1, i+2, i+9, i+10, i+11, i+18, i+19, i+20]
	    problem.addConstraint(AllDifferentConstraint(), box)
	print(problem.getSolution())
