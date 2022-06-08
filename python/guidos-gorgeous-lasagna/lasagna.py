EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_layers):
    """ Calculate the time for making number_layers
    :param number_layers : int number of layers of the lasagna
    :return : int total time to make number of layers
    Function that takes the number of layers as an argument and returns
    how many minutes you need to make the lasagna bases on the `PREPARATION_TIME`
    """
    return number_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_layers, elapsed_bake_time):
    """ Calculate the total number of minutes you've been cooking
    :param number_layers : int number of layers of the lasagna
    :param elapsed_bake_time : int time already spent baking
    :return : int total minutes you've been cooking
    Function that takes the number of layers and elapsed bake time as arguments 
    and returns how many minutes you've been cooking
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_layers)
