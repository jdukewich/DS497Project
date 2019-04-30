import sys

from helper_functions import read_standard_puzzles, read_jumbo_puzzles, solve_puzzles
from csp import HeuristicRecursiveBacktrackingSolver


def main():
    """
    This script performs an execution time test of a CSP algorithm on a set of sudokus with given heuristic(s).

    Usage: python tester.py subsquare_length [--variable var_heuristic_id] [--value val_heuristic_id]

    subsquare_length: n = 3 or n = 4 for 9x9 or 16x16 sets, respectively
    var_heuristic_id: string identifier of the variable heuristic to be used
    val_heuristic_id: string identifier of the value heuristic to be used
    """
    if len(sys.argv) >= 2:
        try:
            subsquare_length = int(sys.argv[1])
        except ValueError:
            print('Error: bad input.')
            return

        try:
            var_heuristic_id = sys.argv[sys.argv.index('--variable') + 1]
        except (ValueError, IndexError):
            var_heuristic_id = None

        try:
            val_heuristic_id = sys.argv[sys.argv.index('--value') + 1]
        except (ValueError, IndexError):
            val_heuristic_id = None

        # instantiate solver with specified heuristics
        heuristic_solver = HeuristicRecursiveBacktrackingSolver(variable_heuristic_id=var_heuristic_id,
                                                                value_heuristic_id=val_heuristic_id)

        # generate test puzzles
        test_puzzles = []

        if subsquare_length == 3:
            test_puzzles = read_standard_puzzles('standard_size_sudokus.csv')
        elif subsquare_length == 4:
            test_puzzles = read_jumbo_puzzles('jumbo_size_sudokus.csv')
        else:
            print('Error: bad subsquare size.')
            return

        solve_puzzles(test_puzzles, heuristic_solver)

    else:
        print('Error: bad input.')
        return


# run main function
if __name__ == '__main__':
    main()
