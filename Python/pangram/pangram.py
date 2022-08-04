import string


def is_pangram(sentence):
    #sentence = str(input()).lower()
    sentence = sentence.lower()
    alphabet = list(string.ascii_lowercase)
    letters_in_sentence = []
    for letter in alphabet:
        if letter in sentence:
            letters_in_sentence.append(letter)
        else:
            continue
    if (len(letters_in_sentence) == len(alphabet)) == True:
        print("True " + str(len(letters_in_sentence)) + "/" + str(len(alphabet)))
    else:
        print("False " + str(len(letters_in_sentence)) + "/" + str(len(alphabet)))
    return len(letters_in_sentence) == len(alphabet)
