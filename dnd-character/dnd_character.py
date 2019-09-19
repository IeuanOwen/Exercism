from random import randrange
from math import floor

def modifier(number):
    print ("Modifier: ", floor(((number - 10) / 2)))
    return floor((number - 10)/2)


class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.charisma = self.ability()
        self.wisdom = self.ability()
        self.intelligence = self.ability()
        self.constitution = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = [randrange(1,7) for i in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)
