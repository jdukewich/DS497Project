from views import *
from board import *

def main():
	
	b1 = Board(size=9)
	view1 = TextView(b1)
	view1.print_board()

	b2 = Board(size=16)
	view2 = TextView(b2)
	view2.print_board()

	b3 = Board(size=16, board=soln2)
	view3 = TextView(b3)
	view3.print_board()

if __name__ == '__main__':
	main()