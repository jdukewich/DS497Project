import csv

from constraint import Problem, AllDifferentConstraint
from classes import Board

from datetime import datetime


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


def read_jumbo_puzzles(input_file):
    """
    Reads multiple 4x4 sudoku puzzle in csv format.

    :param input_file: name of input file to be read
    :return: an array of 2D array boards
    """
    read_puzzles = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            to_add = []
            for i in range(16):
                add_row = []
                for j in range(16):
                    add_row.append(int(row[16*i+j]))
                to_add.append(add_row)
            read_puzzles.append(to_add)
    return read_puzzles


def read_big_puzzle(input_file):
    """
    Reads one 4x4 sudoku puzzle in csv format.

    :param input_file: name of input file to be read
    :return: an array of 2D array boards

    NOTE: did not make it into the final version of the project :(
    """
    puzzle = []
    infile = csv.reader(open(input_file), delimiter=',')

    for row in infile:
        puzzle.append([int(entry) for entry in row])

    return puzzle


def solve_puzzles(puzzles, solver):
    """
    Solves an array of sudoku puzzles, recording runtime.

    :param puzzles: an array of 2D array boards
    :param solver: the CSP solver to be used
    :return: none
    """
    fail_count = 0
    start_time = datetime.now()     # start timer (for runtime)

    for puzzle in puzzles:
        # initialize Board
        b = Board(puzzle)

        sudoku = Problem(solver)      # initialize CSP with custom solver

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

        if sln:
            # assign solved values
            for index, value in sln.items():
                b.set_value(index, value)
        else:
            fail_count += 1

    # perform/display runtime calculation
    runtime = datetime.now() - start_time
    print("Runtime: {} seconds ({} failed)".format(runtime.total_seconds(), fail_count))
