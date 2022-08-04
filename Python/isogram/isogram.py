def is_isogram(string):
    lst = [i for i in string.lower() if i.isalpha()]
    return len(set(lst)) == len(lst)
