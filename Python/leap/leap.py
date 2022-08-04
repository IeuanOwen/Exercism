
def is_leap_year():
    year = int(input("Number: "))
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        result = (str(year) + " is a leap year!")
    else:
        result = (str(year) + " is not a a leap year!")
    print(result)
    return result

is_leap_year()

"""
BEST SOLUTION
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
"""