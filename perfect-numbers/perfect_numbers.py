
def get_factors(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0 and n != i:
            factors.append(i)
    return sum(factors)

def classify(number):
    if number <= 0:
        raise ValueError("Number must be greater than 0")
    total = get_factors(number)
    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    else:
        return "deficient"