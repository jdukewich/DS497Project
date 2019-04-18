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
    """Class representing a sudoku board."""

    def __init__(self, preset):
        """
        Constructor for the board.

        :param preset: n^2 x n^2 (n=1,2,...) 2D array containing the initial values of the board.
        """

        self.board_size = len(preset)
        self.subsquare_size = math.sqrt(self.board_size)
        self.board = preset

    def __str__(self):
        """
        String representation for the board.

        :return a printable representation of the board
        """
        string_board = ''

        for row in range(self.board_size):
            for col in range(self.board_size):
                val = self.board[row][col]

                string_board += ' '

                if val != 0:
                    if val < 10:
                        string_board += ' '
                    string_board += str(val) + ' '
                else:
                    string_board += ' ' * 3

                # add vertical spacers between subsquares
                string_board += ('|' if col < self.board_size - 1 and (col + 1) % self.subsquare_size == 0 else '')

            # horizontal spacers between subsquares
            string_board += '\n' + (('— ' * 2 * self.board_size + '\n') if row < self.board_size - 1 and (row + 1) % self.subsquare_size == 0 else '\n')

        return string_board

    @staticmethod
    def subsquare_index(board, row, col):
        """
        Return the subsquare # of a position on the board.

        A subsquare is a sub-grouping of numbers (there are 9 for a 3x3 board) that must be all different together.
        They are numbered across as follows:
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
        """Return list of entries in subsquare of index sq (...size)."""

        sq = []

        for row in range(self.board_size):
            for col in range(self.board_size):
                if Board.subsquare_index(self, row, col) == sq_index:
                    sq.append(self.board[row][col])

        return sq

    def get_value(self, coords):
        """
        Return the value stored in the coordinate tuple.

        :param coords: (row, col) tuple, where row, col < board size
        """
        if coords[0] < self.board_size and coords[1] < self.board_size:
            return self.board[coords[0]][coords[1]]
        return 0

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
