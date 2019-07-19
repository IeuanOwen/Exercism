def is_armstrong_number(number):
    power = len(str(number))
    numbers = [int(n) for n in str(number)]
    powered_nums = sum([num ** power for num in numbers])
    if powered_nums == number:
        return True
    else:
        return False