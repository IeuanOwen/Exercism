def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strings are not the same length")
    return sum([1 for x, y in zip(strand_a, strand_b) if x != y])
