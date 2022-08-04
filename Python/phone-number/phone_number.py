import re

class PhoneNumber:
    def __init__(self, num):
        self.formatted_num = self.format(num)
        self.number = self.formatted_num
        self.area_code = self.number[:3]
        if len(self.number) != 10:
                raise ValueError("Number not the right length")
        if int(self.number[3]) < 2 or int(self.number[0]) < 2:
            raise ValueError("Area Code must start with 2")

    def format(self, num):
        num = num.strip('+1')
        num = num.replace(' ', '')
        num = re.sub('[aA-zZ.)(-]', '', num)
        return num

    def pretty(self):
        numlist = list(self.formatted_num)
        numlist[0] = f'({numlist[0]}'
        numlist[2] = f'{numlist[2]}) '
        numlist[5] = f'{numlist[5]}-'
        return "".join(numlist)
