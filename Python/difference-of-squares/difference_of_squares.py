def square_of_sum(count):
    iniresult = 0
    for i in range(count + 1):
        iniresult += i
    result = iniresult * iniresult
    return result


def sum_of_squares(count):
    result = 0
    for i in range(count + 1):
        result += (i*i)
    return result


def difference(count):
    diff = square_of_sum(count) - sum_of_squares(count)
    return diff

