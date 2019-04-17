from views import *
from board import *
from test import *

def main():
	
	# Makes array of arrays that can be used to test sudoku
	# For instance, unsolved[0] will be a 9 x 9 array of an unsolved sudoku
	unsolved = []
	with open('puzzles.csv') as f:
	    for line in f:
	        to_add = [[None for i in range(9)] for j in range(9)]
	        for i in range(len(line)-2):
	            to_add[i//9][i%9] = int(line[i]) if line[i] != '.' else ' '
	        unsolved.append(to_add)

	b1 = Board(size=9)
	view1 = TextView(b1)
	view1.print_board()

	b2 = Board(size=16)
	view2 = TextView(b2)
	view2.print_board()

	bthree = make_board_from_dict(test())
	b3 = Board(size=9, board=bthree)
	view3 = TextView(b3)
	view3.print_board()

if __name__ == '__main__':
	main()