def two_fer(name = "you"):
    if name is None or type(name) != str:
        raise Exception("Name must be a string")
    string = f"One for {name}, one for me."
    return string