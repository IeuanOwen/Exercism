"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if elapsed_bake_time > 40:
        return "Your lasagna has burned"
    elif elapsed_bake_time == EXPECTED_BAKE_TIME:
        return "Lasagna Ready!!!"
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """
    :param layers: int - number of layers your lasagna should have.
    :return: int - time taken to create lasagna in mins derived from 'PREPARATION_TIME'.

    Function that takes the number of layers you want to add to your Lasagna
    as an argument and returns how many minuetes the lasagna will take to prepare.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    :param layers: int - number of layers your lasagna should has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - time spent creating lasagna in mins so far.

    Function that takes the number of layers you want to add to your lasagna
    and how many minuets it has been cooking so far as arguments and returns how
    many minuetes you have spent preparing the lasagna so far.
    """
    prep_time = preparation_time_in_minutes(layers)
    return elapsed_bake_time + prep_time



# TODO: define the 'elapsed_time_in_minutes()' function
