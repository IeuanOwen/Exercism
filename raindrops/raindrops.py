def convert(number):
    noFactor = str(number)
    answer = ""
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0: #tests if any of the values are a factor
        answer = noFactor
    else:
        if number % 3 == 0:
            answer = answer + "Pling"
        if number % 5 == 0:
            answer = answer + "Plang"
        if number % 7 == 0:
            answer = answer + "Plong"
    return answer