import sys


class Main:
    def __init__(self, input_list):
        """
        Calculator function process
        :param input_list: List[] of an operator, and at least two floating-point numbers
        """
        choice = input_list[0]
        self.total = 0
        self.values = input_list[1:]

        match choice:
            case "add":
                self.total = self.add()
            case "subtract":
                self.total = self.subtract()
            case "multiply":
                self.total = self.multiply()
            case "divide":
                self.total = self.divide()

    def add(self):
        """
        Summation of all values less than zero
        :return: Summation as a float
        """
        summation = 0

        if len(self.values) > 0:
            if self.values[0] < 0:  # skip non-negative value
                summation = self.values[0]

            if len(self.values[1:]) > 0:  # continue if more than one value passed
                self.values = self.values[1:]

                for current_value in self.values:
                    if current_value < 0:  # skip non-negative values
                        summation += current_value

        return float(summation)

    def subtract(self):
        """
        Difference of all values larger than zero
        :return: Difference as a float
        """
        difference = 0

        if len(self.values) > 0:
            if self.values[0] > 0:  # skip non-positive values
                difference = self.values[0]

            if len(self.values[1:]) > 0:  # continue if more than one value passed
                self.values = self.values[1:]

                for current_value in self.values:
                    if current_value > 0:  # skip non-positive values
                        difference -= current_value

        return float(difference)

    def multiply(self):
        """
        Product of all non-zero values
        :return: Product as a float
        """
        product = 0

        if len(self.values) > 0:
            if self.values[0] != 0:  # skip zero
                product = self.values[0]

                if len(self.values[1:]) > 0:  # continue if more than one value passed
                    self.values = self.values[1:]

                    for current_value in self.values:
                        if current_value != 0:  # skip zeroes
                            product *= current_value

        return float(product)

    def divide(self):
        """
        Quotient of all non-zero values
        :return: Quotient as a float
        """
        quotient = 0

        if len(self.values) > 0:
            try:
                quotient = self.values[0]

                if len(self.values[1:]) > 0:  # continue if more than one value passed
                    self.values = self.values[1:]

                    for current_value in self.values:
                        quotient /= current_value

            except ZeroDivisionError:
                sys.exit('Cannot divide by 0')

        return float(quotient)

    def get_total(self):
        return self.total


if __name__ == "__main__":
    Main(sys.argv)
