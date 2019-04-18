import csv

from constraint import Problem, AllDifferentConstraint
from classes import Board

from datetime import datetime

# preset puzzle
p = [
    [0, 0, 0, 0, 8, 2, 0, 0, 9],
    [0, 2, 9, 0, 4, 0, 3, 6, 0],
    [3, 0, 0, 0, 0, 9, 0, 1, 0],
    [1, 0, 0, 0, 9, 0, 0, 3, 2],
    [0, 7, 2, 0, 5, 0, 1, 8, 0],
    [4, 3, 0, 0, 7, 0, 0, 0, 5],
    [0, 8, 0, 9, 0, 0, 0, 0, 1],
    [0, 9, 7, 0, 1, 0, 8, 4, 0],
    [5, 0, 0, 8, 2, 0, 0, 0, 0],

]

jordan = [
    [0, 0, 0, 0, 0, 0, 0, 7, 2],
    [0, 0, 0, 0, 4, 9, 8, 0, 0],
    [3, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 4, 1, 5],
    [0, 0, 4, 1, 0, 0, 7, 0, 0],
    [1, 6, 0, 3, 0, 0, 0, 2, 0],
    [6, 0, 0, 0, 5, 0, 0, 0, 4],
    [5, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 9, 0, 0, 0, 0],
]

p_hard = [
    [0, 2, 0, 0, 1, 16, 4, 0, 0, 10, 0, 0, 0, 0, 12, 0],
    [10, 0, 0, 11, 0, 6, 0, 0, 2, 0, 0, 0, 0, 14, 0, 0],
    [0, 12, 0, 0, 0, 0, 0, 8, 0, 0, 3, 0, 2, 0, 0, 10],
    [0, 0, 0, 15, 0, 0, 5, 0, 1, 0, 0, 0, 0, 0, 4, 0],
    [11, 0, 12, 0, 0, 14, 0, 6, 0, 1, 0, 3, 0, 10, 0, 4],
    [0, 13, 0, 7, 10, 0, 3, 0, 0, 0, 0, 16, 0, 0, 5, 0],
    [16, 0, 15, 0, 12, 0, 0, 0, 8, 0, 0, 0, 9, 0, 0, 2],
    [0, 0, 0, 9, 0, 11, 0, 0, 0, 0, 0, 15, 0, 3, 0, 0],
    [0, 8, 4, 0, 11, 0, 12, 2, 0, 5, 0, 0, 14, 0, 9, 0],
    [7, 0, 10, 0, 0, 0, 0, 0, 3, 0, 0, 9, 0, 15, 0, 11],
    [0, 6, 0, 0, 15, 0, 0, 16, 0, 0, 10, 0, 12, 0, 13, 0],
    [0, 0, 0, 12, 0, 1, 0, 0, 0, 16, 0, 13, 0, 6, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 10, 13, 9, 0, 5, 0, 12, 0, 0, 15, 0, 8, 0],
    [0, 7, 0, 0, 8, 0, 14, 0, 0, 0, 15, 0, 0, 0, 0, 0],
    [14, 0, 3, 0, 0, 7, 0, 0, 0, 0, 13, 2, 0, 4, 0, 16],
]


def read_standard_puzzles(input_file):
    """
    Reads puzzles from 3x3 csv format.

    :param input_file: name of input file to be read
    :return: an array of 2D array boards
    """
    puzzles = []
    with open(input_file) as f:
        for line in f:
            to_add = [[None for i in range(9)] for j in range(9)]
            for i in range(len(line)-2):
                to_add[i // 9][i % 9] = int(line[i]) if line[i] != '.' else 0
            puzzles.append(to_add)

    return puzzles


def read_big_puzzle(input_file):
    """
    Reads one 4x4 sudoku puzzle in csv format.

    :param input_file: name of input file to be read
    :return: an array of 2D array boards
    """
    puzzle = []
    infile = csv.reader(open(input_file), delimiter=',')

    for row in infile:
        print(row)
        puzzle.append([int(entry) for entry in row])

    return puzzle


def solve_puzzles(puzzles):
    """
    Solves an array of sudoku puzzles, outputting each and recording runtime.

    :param puzzles: an array of 2D array boards
    :return: none
    """
    start_time = datetime.now()     # start timer (for runtime)

    for puzzle_index in range(len(puzzles)):
        # initialize Board
        b = Board(puzzles[puzzle_index])

        # log initial
        print('Puzzle {} (Initial)\n'.format(puzzle_index + 1))
        print(b)
        print("Consistent: " + str(b.check_valid()))
        print('\n\n\n')

        sudoku = Problem()      # initialize CSP

        # add variables for each square, indexed 1...size^2
        for index in range(b.board_size ** 2):
            value = b.get_value(index)

            if value == 0:
                sudoku.addVariable(index, range(1, b.board_size + 1))
            else:
                sudoku.addVariable(index, [value])

        # add uniqueness constraints to each row, column, and subsquare
        for i in range(b.board_size):
            sudoku.addConstraint(AllDifferentConstraint(), [el[0] for el in b.row(i)])
            sudoku.addConstraint(AllDifferentConstraint(), [el[0] for el in b.col(i)])
            sudoku.addConstraint(AllDifferentConstraint(), [el[0] for el in b.subsquare(i)])

        sln = sudoku.getSolution()      # solve CSP

        # assign solved values
        for index, value in sln.items():
            b.set_value(index, value)

        # log solution
        print('Puzzle {} (Solved)\n'.format(puzzle_index + 1))
        print(b)
        print("Valid: " + str(b.check_valid()))
        print('\n\n\n')

    # perform/display runtime calculation
    runtime = datetime.now() - start_time
    print("Runtime: {} seconds".format(runtime.total_seconds()))


# Solve 100 3x3 puzzles
# unsolved = read_standard_puzzles('puzzles.csv')
# solve_puzzles(unsolved)

unsolved = read_big_puzzle('mega_puzzle2.csv')
solve_puzzles([unsolved])
