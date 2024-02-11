import sys


def add(values):
    """
    Summation of all values less than zero
    :return: Summation as a float
    """
    summation = 0

    temp_list = []
    for current_value in values:
        if current_value < 0:
            temp_list.append(current_value)
    values = temp_list

    if len(values) > 0:
        summation = values[0]

        if len(values[1:]) > 0:  # continue if more than one value passed
            values = values[1:]

            for current_value in values:
                summation += current_value

    return float(summation)


def subtract(values):
    """
    Difference of all values larger than zero
    :return: Difference as a float
    """

    temp_list = []
    for current_value in values:
        if current_value > 0:
            temp_list.append(current_value)
    values = temp_list

    if len(values) > 0:
        difference = values[0]

        if len(values[1:]) > 0:  # continue if more than one value passed
            values = values[1:]

            for current_value in values:
                if current_value > 0:  # skip non-positive values
                    difference -= current_value

        return float(difference)
    else:
        return float(0)


def multiply(values):
    """
    Product of all non-zero values
    :return: Product as a float
    """

    temp_list = []
    for current_value in values:
        if current_value != 0:
            temp_list.append(current_value)
    values = temp_list

    if len(values) > 0:
        product = values[0]

        if len(values[1:]) > 0:  # continue if more than one value passed
            values = values[1:]

            for current_value in values:
                product *= current_value

        return float(product)
    else:
        return float(0)


def divide(values):
    """
    Quotient of all non-zero values
    :return: Quotient as a float
    """
    quotient = 0

    temp_list = [values[0]]
    values = values[1:]

    for current_value in values:
        if current_value != 0:
            temp_list.append(current_value)
        else:
            sys.exit('Cannot divide by 0')

    values = temp_list

    if len(values) > 0:
        quotient = values[0]

        if len(values[1:]) > 0:  # continue if more than one value passed
            values = values[1:]

            for current_value in values:
                quotient /= current_value

    return float(quotient)
