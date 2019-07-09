import itertools

def valid_sides(sides):
    """This function validates the input list"""
    if any(side == 0 for side in sides):
        return False
    for x, y, z in itertools.combinations(sides, 3):
        if (x + y) < z or (y + z) < x or (z + x) < y:
            return False
    else:
        return True


def is_equilateral(sides):
    for x, y, z in itertools.combinations(sides, 3):
        res = valid_sides(sides)
        if not res:
            return False
        if x == y and x == z:
            return True
        else:
            return False


def is_isosceles(sides):
    for x, y, z in itertools.combinations(sides, 3):
        res = valid_sides(sides)
        if not res:
            return False
        if x == y or y == z or x == z:
            return True
        else:
            return False


def is_scalene(sides):
    for x, y, z in itertools.combinations(sides, 3):
        res = valid_sides(sides)
        if not res:
            return False
        if x != y and x != z and y != z:
            return True
        else:
            return False