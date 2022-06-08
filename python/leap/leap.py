"""Calculate if a year is a leap year or not."""


def leap_year(year):
    """Determine if a year is a leap year or not.

    :param year: (int) the year to test
    :return: (bool) True if the year is a leap year or False
    """

    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100:
        return True
    else:
        return False
