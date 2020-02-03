
def first_verse_line(num, plur):
    """Format string for verse line 1"""
    num2 = num if num != "No more" else "no more"
    line = f"{num} {plur} of beer on the wall, {num2} {plur} of beer."
    return line

def sec_verse_line(num, plural="bottles", var="one"):
    """Format string for verse line 2"""
    line = f"Take {var} down and pass it around, {num} {plural} of beer on the wall."
    return line

def recite(start, take=1):
    last_line = "Go to the store and buy some more, 99 bottles of beer on the wall."
    song = []

    for i in range(take):
        plural = "bottles" if start != 1 else "bottle"

        if start != 0:
            song.append(first_verse_line(start, plural))
            num = start - 1
            if start > 2:
                song.append(sec_verse_line(num))

            elif start == 2:
                song.append(sec_verse_line(num, "bottle"))
            else:
                song.append(sec_verse_line("no more", var="it"))
            start -= 1
        else:
            song.append(first_verse_line("No more", plural))
            song.append(last_line)

        if start != 0 and i != take-1:
            song.append("")

    return song
