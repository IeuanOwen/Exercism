def is_isogram(string):
    lst = [i for i in string.lower() if i.isalpha()]
    s = set(lst)
    return len(s) == len(lst)
