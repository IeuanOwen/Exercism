def convert(number):
    answer = ""
    if number % 3 == 0:
        answer = answer + "Pling"
    if number % 5 == 0:
        answer = answer + "Plang"
    if number % 7 == 0:
        answer = answer + "Plong"
    return answer if answer else str(number) #returns value of answer variable or the number if answer is empty