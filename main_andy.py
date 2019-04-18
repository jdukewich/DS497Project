from constraint import Problem, AllDifferentConstraint

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

b = Board(p)
print(b)
print(b.check_valid())

sudoku = Problem()

# add variables
for row in range(b.board_size):
    for col in range(b.board_size):
        sudoku.addVariable(b.get_value(row, col).index, range(1, b.board_size + 1))

for i in range(b.board_size):
    sudoku.addConstraint(AllDifferentConstraint(), [r.index for r in b.row(i)])
    sudoku.addConstraint(AllDifferentConstraint(), [c.index for c in b.col(i)])
    sudoku.addConstraint(AllDifferentConstraint(), [sq.index for sq in b.subsquare(i + 1)])

sln = sudoku.getSolution()

for index, value in sln.items():
    b.set_entry(index, value)

print(b)
print(b.check_valid())

