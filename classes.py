import math

DEFAULT_SIZE = 9        # standard sudoku size


class Square:
    """
    Class representing a sudoku board square.
    """

    def __init__(self, index, row, col, subsquare, value):
        self.index = index
        self.row = row
        self.col = col
        self.subsquare = subsquare
        self.value = value

    def __repr__(self):
        return str(self.value)


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
        self.board = []

        for r in range(self.board_size):
            row = []
            for c in range(self.board_size):
                row.append(Square(r * self.board_size + c,
                                  r,
                                  c,
                                  int((c // self.subsquare_size) +
                                      self.subsquare_size * (r // self.subsquare_size) + 1),
                                  preset[r][c]))
            self.board.append(row)

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
        """Return list of entries in row of board (0...size-1)."""
        if row <= self.board_size:
            return self.board[row]
        else:
            return []

    def col(self, col):
        """Return list of entries in col of board (0...size-1)."""
        if col <= self.board_size:
            return [el[col] for el in self.board]
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

    def values_list(self):
        """Return 1-D representation of board."""
        entries = []

        for row in range(self.board_size):
            for col in range(self.board_size):
                entries.append(self.board[row][col])

        return entries

    def get_value(self, row, col):
        """Return the current value stored at (row, col)."""
        return self.board[row][col]

    def set_entry(self, index, value):
        """Set the entry located at the index to a particular value."""
        row = index // self.board_size
        col = index % self.board_size

        self.board[row][col].value = value

    def check_valid(self):
        """Return whether the board is valid."""
        for i in range(self.board_size):
            # check rows
            r = [entry.value for entry in list(filter(lambda x: x.value != 0, self.row(i)))]

            if len(r) != len(set(r)):
                return False

            # check columns
            c = [entry.value for entry in list(filter(lambda x: x.value != 0, self.col(i)))]

            if len(c) != len(set(c)):
                return False

            # check subsquares
            sq = [entry.value for entry in list(filter(lambda x:x.value != 0, self.subsquare(i + 1)))]

            if len(sq) != len(set(sq)):
                return False

        return True