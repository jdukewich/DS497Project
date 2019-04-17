import math


class Board:
    """Class representing a sudoku board."""

    def __init__(self, size=9, board=None):
        self.size = size
        self.board = board
        if self.board is None:
            self.board = self.__generate_board()

    def __generate_board(self):
        """Fill """
        board = [[i+j*self.size for i in range(self.size)] for j in range(self.size)]
        return board

    def is_filled(self):
        for i in range(self.size**2):
            if self.board[i//self.size][i%self.size] == ' ':
                return False
        return True

    def valid_rows(self):
        for row in range(self.size):
            current_list = set()
            for col in range(self.size):
                if self.board[row][col] in current_list:
                    return False
                elif self.board[row][col] != ' ':
                    current_list.add(self.board[row][col])
        return True

    def valid_cols(self):
        for col in range(self.size):
            current_list = set()
            for row in range(self.size):
                if self.board[row][col] in current_list:
                    return False
                elif self.board[row][col] != ' ':
                    current_list.add(self.board[row][col])
        return True

    def valid_boxes(self):
        for i in range(0, self.size, int(math.sqrt(self.size))):
            for j in range(0, self.size, int(math.sqrt(self.size))):
                current_list = set()
                for k in range(int(math.sqrt(self.size))):
                    for l in range(int(math.sqrt(self.size))):
                        if self.board[i+k][j+l] in current_list:
                            return False
                        elif self.board[i+k][j+l] != ' ':
                            current_list.add(self.board[i+k][j+l])
        return True

    def is_valid(self):
        return self.valid_rows() and self.valid_cols() and self.valid_boxes()
