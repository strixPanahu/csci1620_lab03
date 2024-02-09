"""

    CSCI 1620 001/851
    Professor Owora
    Week 03 - Lab 03
    05/02/2024
"""

import sys
import formulas


class Main:
    def __init__(self, input_raw):
        """
        Initialise console-level calculator application
        :param input_raw: List[] of an operator, and at least two numbers
        """
        self.input_list = []
        self.validate_input(input_raw)
        self.calculation = formulas.Main(self.input_list)

    def validate_input(self, input_raw):
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

        self.input_list = input_raw

    def get_input_raw(self):
        return self.input_list

    def get_output(self):
        output = "Answer = {:.2f}"
        return output.format(self.calculation.get_total())


if __name__ == "__main__":
    instance = Main(sys.argv)
    print(instance.get_output())
