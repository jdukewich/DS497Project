"""
Support two types of views (eventually): 
		- text-based (useful for command line troubleshooting)
		- GUI based 
"""
import math
from board import Board


class TextView:
	def __init__(self, board=None):
		if board is None:
			self.b = Board()
		else:
			self.b = board

	def print_board(self):

		sq_size = int(math.sqrt(self.b.size))

		print('-'*(4*(self.b.size+sq_size)-3))

		for i in range(sq_size):
			for j in range(i*sq_size, (i+1)*sq_size):
				# beginning of row
				print('|', end='')
				for k in range(sq_size):
					for l in range(k*sq_size, (k+1)*sq_size):
						print('{:^3}'.format(self.b.board[j][l]), end='|')
					if k != sq_size-1:
						print('   ', end='|')
				print()
			print('-'*(4*(self.b.size+int(math.sqrt(self.b.size)))-3))


class GUIView:
	def __init__(self):
		pass
