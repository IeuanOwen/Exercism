
def on_square(number):
    if not (0 < number <= 64):
        raise ValueError("Number must be between 1 & 64")
    amount = 2**(number-1)
    return amount

def total_after(number):
    if not (0 < number <= 64):
        raise ValueError("Number must be between 1 & 64")
    grainlist = []
    for i in range(1, number+1):
        grainlist.append(on_square(i))
    total = sum(grainlist)
    for i in grainlist:
        print(f"Grains on square {grainlist.index(i)+1} = {i}")
    print("Total of grains = ", total)
    return total



