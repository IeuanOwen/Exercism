

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strings are not the same length")
    diff = 0
    for x, y in zip(strand_a, strand_b):
        print(x)
        print(y)
        if x != y:
            diff += 1
    print(diff)
    return diff

