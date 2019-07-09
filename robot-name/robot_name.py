import random
import string


class Robot(object):

    def __init__(self):
        self.name = Robot.new_robot(self)
        pass

    def new_robot(self):
        name = NameGenerator.generator(self)
        print('My Name is ' + name)
        return name


class NameGenerator:

    def __init__():
        NameGenerator.generator()
        pass


    def generator(self):
        namelist = []
        for i in range(2):
            letter = random.choice(string.ascii_uppercase)
            namelist.append(letter)
        for i in range(3):
            number = random.choice(string.digits)
            namelist.append(number)
        robotname = "".join(namelist)
        print("generated = "+robotname)
        return robotname


Robot.__init__('test')
