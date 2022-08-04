from itertools import permutations

def slices(series, length):
    """Slices a string into smaller chunks of a given length"""
    slice_list = []
    if not series or length <= 0 or length > len(series):
        raise ValueError("Invalid Input")

    for i in range(len(series)):
        item = series[i:(i + length)]
        slice_list.append(item) if len(item) == length else slice_list
    return slice_list



def Permutations(series, length):
    """Not part of exercism - returns all possible combinations of letters in string of given length"""
    perm_list = []
    if not series or length <= 0 or length > len(series):
        raise ValueError("Invalid Input")

    perms = permutations(series, length)
    for perm in perms:
        perm_list.append("".join(perm))
    return perm_list
