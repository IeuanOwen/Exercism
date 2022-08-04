"""Return a list of all the prime factors of a number."""

def factors(startnum):
    prime_factors = []
    factor = 2 # Begin with a Divisor of 2
    while startnum > 1:
        if startnum % factor == 0:
            prime_factors.append(factor)
            startnum /= factor # divide the startnum by the factor
        else: # If the divisor is not a factor increase it by 1
            factor += 1
    return prime_factors
