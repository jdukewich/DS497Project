import math

DEFAULT_SIZE = 9        # standard sudoku size


class Board:
    """
    Class representing a sudoku board.

    The board is n x n in size containing n subsquares of size sqrt(n) x sqrt(n).
    """

    def __init__(self, preset):
        """
        Constructor for the board.

        size: the size of the sudoku square. Must be a square number (4, 9, 16, etc.). Defaults to standard 3x3
        preset: A size x size 2D array containing the initial values of the board.
        """

        self.board_size = len(preset)
        self.subsquare_size = math.sqrt(self.board_size)
        self.board = preset

    def __str__(self):
        """String representation for the board."""
        b = ''

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != 0:
                    b += str(self.board[row][col])
                else:
                    b += ' ' * len(str(self.board[row][col]))

                # vertical spacers between subsquares
                b += (' |' if col < self.board_size - 1 and (col + 1) % self.subsquare_size == 0 else '') + '\t'

            # horizontal spacers between subsquares
            b += '\n' + (('— ' * 2 * self.board_size + '\n') if row < self.board_size - 1 and (row + 1) % self.subsquare_size == 0 else '\n')

        return b

    @staticmethod
    def subsquare_index(board, row, col):
        """
        Return the subsquare # of a position on the board.

        A subsquare is a sub-grouping of numbers (there are 9 for a 3x3 board) that must be all different together.
        They are numberd across as follows:
        1 2 3
        4 5 6
        7 8 9
        Where each index represents a group of additional numbers.
        """
        return int((col // board.subsquare_size) + board.subsquare_size * (row // board.subsquare_size) + 1)

    def row(self, row):
        """Return list of entries in row of board (1...size)."""
        if row <= self.board_size:
            return self.board[row - 1]
        else:
            return []

    def col(self, col):
        """Return list of entries in col of board (1...size)."""
        if col <= self.board_size:
            return [el[col - 1] for el in self.board]
        else:
            return []

    def subsquare(self, sq_index):
        """Return list of entries in subsquare of index sq (1...sqrt(size))."""

        sq = []

        for row in range(self.board_size):
            for col in range(self.board_size):
                if Board.subsquare_index(self, row, col) == sq_index:
                    sq.append(self.board[row][col])

        return sq


p = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 0, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 0, 9],
    [1, 2, 3, 0, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

p_big = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
]

b = Board(p_big)
print(b)
print(b.col(9))
print(b.row(2))
print(b.subsquare(5))
