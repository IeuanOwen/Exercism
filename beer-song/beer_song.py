def recite(start, take=1):
    phrase1 = "{} {} of beer on the wall, {} {} of beer."
    phrase_sec_line1 = "Take {} down and pass it around, {} {} of beer on the wall."
    phrase2 = "No more bottles of beer on the wall, no more bottles of beer."
    phrase2_sec_line = "Go to the store and buy some more, 99 bottles of beer on the wall."

# figure out how to loop in reverse throught the range of take
    for i in range(take):
        start = take
        if start == 0:
            print(phrase2)
            return [phrase2, phrase2_sec_line]
        elif start == 1:
            phrase = [phrase1.format(start, "bottle", start, "bottle"), phrase_sec_line1.format("it", "no more", "bottles")]
            print(phrase)
            return phrase
        elif start == 2:
            phrase = [phrase1.format(start, "bottles", start, "bottles"), phrase_sec_line1.format("one", start - 1, "bottle")]
            print(phrase)
            return phrase
        else:
            phrase = [phrase1.format(start, "bottles", start, "bottles"), phrase_sec_line1.format("one", start - 1, "bottles")]
            print(phrase)
            return phrase
