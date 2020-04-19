from collections import Counter as counter

def find_anagrams(word, candidates):
    word = word.lower()
    wordc = counter(word)
    matches = []
    for candidate in candidates:
        candc = counter(candidate.lower())
        if wordc == candc and word != candidate.lower():
            matches.append(candidate)
    return matches
