standardReply = "Whatever."
questionReply = "Sure."
yellReply = "Whoa, chill out!"
silenceReply = "Fine. Be that way!"
loudQuestionReply = "Calm down, I know what I'm doing!"

def hey(phrase):
    phrase = phrase.strip()
    if phrase == "":
        return silenceReply
    elif phrase.endswith("?"):
        if phrase.isupper():
            return loudQuestionReply
        else:
            return questionReply
    elif phrase.isupper():
        return yellReply
    else:
        return standardReply

