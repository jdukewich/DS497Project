"""
Apply heuristics for recursive backtracking solver

"""
import random


def variable_heuristic(domains, vconstraints, heuristic):
    """
    Applies the given heuristic for choosing an unassigned variable

    :param domains: the dict of {variable: [domain values], ...}
    :param vconstraints: dict of {variable: [(constraintObject, [vars in constraint]), ...], ...}
    :param heuristic: a string of which heuristic you want to use
    :return: a list of tuples from the the solver iterates through in order to check variables
    """
    if heuristic == 'degree':
        return degree(vconstraints, domains)
    elif heuristic == 'mrv':
        return mrv(domains)
    elif heuristic == 'random':
        return random_variable(domains)
    # No heuristic
    else:
        return no_var_heur(domains)


def value_heuristic(domain, heuristic):
    """
    Applies the given heuristic checking values in the domain

    :param domain:  an array of the remaining values in the domain for a variable
    :param heuristic: a string of which heuristic you want to use
    :return: an array of remaining values in the domain in a certain order based upon heuristics
    """
    if heuristic == 'random':
        return random_value(domain)
    # No heuristic
    else:
        return domain


# BEGIN SELECT-UNASSIGNED-VARIABLE HEURISTICS
def no_var_heur(domains):
    """
    No heuristic applied here :(

    :param domains: the dict of {variable: [domain values], ...}
    :return: a list of tuples (1, variable) with no specific order
    """
    lst = [
        (1, variable)
        for variable in domains
    ]
    return lst


def degree(vconstraints, domains):
    """
    The degree heuristic is applied, although this technically does nothing for sudoku

    :param vconstraints:
    :param domains: the dict of {variable: [domain values], ...}
    :return: a sorted list of tuples (x, variable) where x is the negative of how many constraints the
    variable is a part of
    """
    lst = [
        (-len(vconstraints[variable]), variable)
        for variable in domains
    ]
    lst.sort()
    return lst


def mrv(domains):
    """
    Minimum remaining values heuristic, seems to work best for our sudoku problem

    :param domains: the dict of {variable: [domain values], ...}
    :return: a sorted list of tuples (x, variable) where x is the number of potential values variable can take
    """
    lst = [
        (len(domains[variable]), variable)
        for variable in domains
    ]
    lst.sort()
    return lst


def random_variable(domains):
    """
    Random sorts the variables, definitely not going to be effective

    :param domains: the dict of {variable: [domain values], ...}
    :return: a shuffled list of tuples (1, variable)
    """
    lst = [
        (1, variable)
        for variable in domains
    ]
    random.shuffle(lst)
    return lst


def degree_and_mrv():
    pass


def mrv_and_random():
    pass


def spatial_locality():
    pass


def temporal_locality():
    pass


# END SELECT-UNASSIGNED-VARIABLE HEURISTICS

# BEGIN SELECT-VALUE-FROM-DOMAIN HEURISTICS
def random_value(domain):
    """
    Randomizes the order of domain values to check

    :param domain: an array of remaining domain values
    :return: the same array but in a shuffled order
    """

    newlst = domain[:]
    random.shuffle(newlst)
    return newlst


def lcv():
    pass


def least_used():
    pass


# END SELECT-VALUE-FROM-DOMAIN HEURISTICS

