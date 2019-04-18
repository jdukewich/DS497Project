from views import *
from board2 import *
from test import *

p_16 = [
	[0, 9, 0, 0, 0, 14, 5, 10, 2, 0, 15, 6, 0, 0, 0, 1],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 5, 0],
	[0, 13, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 9],
	[2, 0, 10, 0, 6, 0, 0, 0, 0, 0, 0, 0, 11, 3, 15, 0],
	[0, 0, 13, 0, 7, 5, 0, 0, 11, 0, 0, 0, 6, 8, 0, 0],
	[7, 11, 0, 0, 3, 0, 1, 6, 5, 14, 10, 9, 0, 0, 0, 0],
	[0, 0, 0, 3, 0, 9, 0, 0, 0, 13, 1, 8, 0, 0, 0, 0],
	[0, 16, 14, 12, 0, 0, 0, 13, 0, 0, 2, 7, 0, 0, 0, 0],
	[0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7],
	[0, 0, 0, 0, 0, 0, 0, 11, 0, 9, 0, 1, 5, 4, 10, 8],
	[0, 7, 3, 0, 2, 6, 0, 0, 0, 12, 0, 13, 1, 0, 0, 15],
	[12, 10, 0, 0, 16, 0, 0, 0, 15, 3, 0, 0, 2, 0, 0, 11],
	[0, 3, 0, 10, 0, 2, 13, 0, 0, 0, 0, 0, 0, 6, 0, 0],
	[13, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 11, 0, 0],
	[0, 8, 0, 0, 11, 7, 3, 0, 0, 0, 14, 0, 0, 0, 0, 0],
	[6, 2, 12, 0, 15, 0, 0, 9, 8, 0, 3, 0, 0, 1, 14, 0],
]


def main():
	
	# Makes array of arrays that can be used to test sudoku
	# For instance, unsolved[0] will be a 9 x 9 array of an unsolved sudoku
	unsolved = []
	with open('puzzles.csv') as f:
		for line in f:
			to_add = [[None for i in range(9)] for j in range(9)]
			for i in range(len(line)-2):
				to_add[i//9][i%9] = int(line[i]) if line[i] != '.' else 0
			unsolved.append(to_add)

	b4 = Board(unsolved[0])
	print(b4)
	soln = Board(test(b4.board))
	print(soln)

	"""
	Note that the python-constraint library gives an error when using the following 16 by 16 board, could
	be my implementation of the library though

	b5 = Board(p_16)
	soln2 = Board(test(b5.board))
	print(soln2)
	"""


if __name__ == '__main__':
	main()
