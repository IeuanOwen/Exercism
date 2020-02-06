import random
import string


class Robot(object):

    def __init__(self):
        self.name = self.new_robot()


    def new_robot(self):
        name = NameGenerator.generator(self)
        return name

    def reset(self):
        newname = NameGenerator.generator(self)
        self.name = newname

class NameGenerator:

    def __init__():
        pass

    def generator(self):
        random.seed(None)
        namelist = []
        for i in range(2):
            letter = random.choice(string.ascii_letters).upper()
            namelist.append(letter)
        for i in range(3):
            number = random.choice(string.digits)
            namelist.append(number)
        robotname = "".join(namelist)
        return robotname
