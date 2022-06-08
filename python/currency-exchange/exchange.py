"""Functions for money manipulations"""


def exchange_money(budget, exchange_rate):
    """Do the conversion of a budget with an exchange rate.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Your initial budget minus the budget you want to exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Compute the total value of your money with your bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """Get the number of a certain bill with your budget.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Get the maximum number of a certain bill after exchange.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    actual_rate = exchange_rate + (exchange_rate * (spread / 100))
    maximum_value = int(((budget / actual_rate) // denomination) * denomination)
    return maximum_value


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """Get the remainder of the money you exchange and your budget with a rate and fees.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    actual_rate = exchange_rate + (exchange_rate * (spread / 100))
    non_exchangeable = int(exchange_money(budget, actual_rate) - exchangeable_value(budget, exchange_rate, spread,
                                                                                    denomination))
    return non_exchangeable
