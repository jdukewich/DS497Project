from constraint import Problem, AllDifferentConstraint
from classes import Board

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

b = Board(p)
print('Initial\n')
print(b)
print("Valid: " + str(b.check_valid()))
print('\n\n\n')

sudoku = Problem()

# add variables for each square, indexed 1...size^2
for index in range(b.board_size ** 2):
    value = b.get_value(index)

    if value == 0:
        sudoku.addVariable(index, range(1, b.board_size + 1))
    else:
        sudoku.addVariable(index, [value])

# add uniqueness constraints to each row, column, and subsquare
for i in range(b.board_size):
    sudoku.addConstraint(AllDifferentConstraint(), b.row(i))
    sudoku.addConstraint(AllDifferentConstraint(), b.col(i))
    sudoku.addConstraint(AllDifferentConstraint(), b.subsquare(i))

# solve CSP
sln = sudoku.getSolution()

# assign solved values
for index, value in sln.items():
    b.set_value(index, value)

print('Solved\n')
print(b)
print("Valid: " + str(b.check_valid()))

