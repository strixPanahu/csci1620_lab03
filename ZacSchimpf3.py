"""

    CSCI 1620 001/851
    Professor Owora
    Week 03 - Lab 03
    05/02/2024
"""

from formulas import *


def __init__(input_raw):
    """
    Initialise console-level calculator application
    :param input_raw: List[] of an operator, and at least two numbers
    """
    input_list = validate_input(input_raw)

    calculation = 0

    match input_list[0]:
        case "add":
            calculation = add(input_list[1:])
        case "subtract":
            calculation = subtract(input_list[1:])
        case "multiply":
            calculation = multiply(input_list[1:])
        case "divide":
            calculation = divide(input_list[1:])

    output = "Answer = {:.2f}"
    print(output.format(calculation))


def validate_input(input_raw):
    """
    Validate raw console-level input and convert floating-point values
    :param input_raw: List[] of an operator, and at least two numbers as strings
    :return: List[] of an operator, and converted floating-point numbers
    """
    acceptable_methods = ["add", "subtract", "multiply", "divide"]

    if len(input_raw) == 0:
        sys.exit("Need to provide operator")

    if (".py" in input_raw[0]
            or "\\" in input_raw[0]
            or "/" in input_raw[0]):  # delete any leading file or dir names
        input_raw = input_raw[1:]

    if input_raw[0] not in acceptable_methods:
        sys.exit("Valid operator names (add, subtract, multiply, divide)")

    if len(input_raw) < 3:
        sys.exit("Need to provide at least two values")

    try:
        index = 1
        while index < len(input_raw):
            input_raw[index] = float(input_raw[index])
            index += 1
    except ValueError:
        sys.exit("Failed to convert input to numeric values")

    return input_raw


if __name__ == "__main__":
    __init__(sys.argv)
