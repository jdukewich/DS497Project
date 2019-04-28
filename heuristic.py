"""
Apply heuristics for recursive backtracking solver

"""
import random
import math


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
    elif heuristic == 'deg+mrv':
        return degree_and_mrv(vconstraints, domains)
    elif heuristic == 'mrv+random':
        return mrv_and_random(domains)
    # No heuristic
    else:
        return no_var_heur(domains)


def value_heuristic(assignments, domains, domain, heuristic):
    """
    Applies the given heuristic checking values in the domain

    :param assignments: a dict of {variable: value, ...}
    :param domains: the dict of {variable: [domain values], ...}
    :param domain:  an array of the remaining values in the domain for the current variable
    :param heuristic: a string of which heuristic you want to use
    :return: an array of remaining values in the domain in a certain order based upon heuristics
    """
    if heuristic == 'random':
        return random_value(domain)
    elif heuristic == 'lcv':
        return lcv(domains, domain)
    elif heuristic == 'least_used':
        return least_used(assignments, domains, domain)
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

    :param vconstraints: dict of {variable: [(constraintObject, [vars in constraint]), ...], ...}
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


def degree_and_mrv(vconstraints, domains):
    """
    Combines degree + MRV heuristic although for a sudoku problem the degree has no effect.

    :param vconstraints: dict of {variable: [(constraintObject, [vars in constraint]), ...], ...}
    :param domains: the dict of {variable: [domain values], ...}
    :return: a sorted list of tuples (x, y variable) where x is the negative of how many constraints the
    variable is a part of, and y is the # of potential values variable can be
    """
    lst = [
        (-len(vconstraints[variable]), len(domains[variable]), variable)
        for variable in domains
    ]
    lst.sort()
    return lst


def mrv_and_random(domains):
    """
    This applies a mix of MRV and randomization. It will sort the variables by MRV initially, then, among
    the variables that have more than 1 remaining value, it will randomize the order of variables with next highest
    remaining values (e.g. 2, or 3 if none with 2 remaining, etc.)

    :param domains: the dict of {variable: [domain values], ...}
    :return: a list sorted by remaining values, with randomization among variables with same # remaining values
    """
    lst = [
        (len(domains[variable]), variable)
        for variable in domains
    ]
    lst.sort()

    # Get array [domain length, ...] in ascending order of domain length != 1
    first = [x[0] for x in lst if x[0] != 1]
    second = [x for x in first if x > first[0]]

    if len(first):
        # Get index of the first domain length != 1 and next index with domain length != 1 and previous
        first_not_one = first[0]
        step_idx = [x[0] for x in lst].index(first_not_one)
        step_idx_two = len(domains)-1

        if len(second):
            second_not_one = second[0]
            step_idx_two = [x[0] for x in lst].index(second_not_one)

        # These lines randomize the order for variables with smallest domain length other than 1
        copy1 = lst[step_idx:step_idx_two]
        random.shuffle(copy1)
        lst[step_idx:step_idx_two] = copy1
    return lst


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


def lcv(domains, domain):
    """
    Sort by the values that affect the least amount of constraints (i.e. sort by number of times each
    value appears in domains)

    :param domains: the dict of {variable: [domain values], ...}
    :param domain: an array of remaining domain values
    :return: an array sorted by the values that constrain the least amount of other variables
    """
    # Initialize array for count of each value
    count = [0 for i in range(int(math.sqrt(len(domains))))]

    # Iterate through domains, counting each time the values are used
    for dom in domains.items():
        for val in dom[1]:
            count[val-1] += 1

    # Now sort by the count of each value
    domain_count = [(count[val-1], val) for val in domain]
    domain_count.sort()
    new_domain = [val[1] for val in domain_count]
    return new_domain


def least_used(assignments, domains, domain):
    """
    Sort the domain of the current value based upon how many times each value has been used already

    :param assignments: a dict of {variable: value, ...}
    :param domains: the dict of {variable: [domain values], ...}
    :param domain: an array of remaining domain values
    :return: a sorted array in ascending order of # of times each value was used
    """
    # Initialize array for count of each value
    count = [0 for i in range(int(math.sqrt(len(domains))))]

    # Iterate through assignments, counting each time the values are used
    for assignment in assignments.items():
        if assignment[1] is not None:
            count[assignment[1]-1] += 1

    # Now copy the # of times values are used into just the values left in the domain of current variable
    domain_count = [(count[val-1], val) for val in domain]
    domain_count.sort()
    new_domain = [val[1] for val in domain_count]
    return new_domain


# END SELECT-VALUE-FROM-DOMAIN HEURISTICS

