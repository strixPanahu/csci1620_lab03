import random
import unittest

import ZacSchimpf3
import formulas


class TestMethods(unittest.TestCase):

    def test_formulas_fail_divide_by_zero(self):
        invalid_values = ["divide", '10', '0']

        with self.assertRaises(SystemExit) as exit_handler:
            test = ZacSchimpf3.Main(invalid_values)
        self.assertEqual(exit_handler.exception.code, "Cannot divide by 0")

    def test_formulas_ok_add_positive_values(self):
        standard_values = ["add", 1, 2, -2, 3]
        return_value = -2

        test = formulas.Main(standard_values)
        self.assertTrue(test.get_total() == return_value, "Failed to validate positive values' sum")

    def test_formulas_ok_init_one_value(self):
        standard_values = [["add", -2],
                           ["subtract", 4],
                           ["multiply", 2],
                           ["divide", 6]]
        return_values = [-2, 4, 2, 6]

        index = 0
        for current_list in standard_values:
            test = formulas.Main(current_list)

            match standard_values[index][0]:
                case "add":
                    self.assertTrue(test.get_total() == return_values[index],
                                    "Failed to validate single value summation")
                case "subtract":
                    self.assertTrue(test.get_total() == return_values[index],
                                    "Failed to validate single value difference")
                case "multiply":
                    self.assertTrue(test.multiply() == return_values[index],
                                    "Failed to validate single value product")
                case "divide":
                    self.assertTrue(test.divide() == return_values[index],
                                    "Failed to validate single value quotient")
            index += 1

    def test_formulas_ok_init_zero_values(self):
        standard_values = [["add"],
                           ["subtract"],
                           ["multiply"],
                           ["divide"]]
        return_value = 0

        for current_list in standard_values:
            test = formulas.Main(current_list)
            self.assertTrue(test.get_total() == return_value, "Failed to validate zero value calculation")

    def test_formulas_ok_multiply_zeroes(self):
        standard_values = ["multiply", 0, 2, 0, -3]
        return_value = -6

        test = formulas.Main(standard_values)
        self.assertTrue(test.get_total() == return_value, "Failed to validate product of List[] with zeroes")

    def test_formulas_ok_subtract_negative_values(self):
        standard_values = ["subtract", -1, -2, 3, -3, 2]
        return_value = 1

        test = formulas.Main(standard_values)

        self.assertTrue(test.get_total() == return_value, "Failed to validate negative values' difference")

    def test_main_fail_invalid_operator(self):
        invalid_values = ["invalid", '0', '1']

        with self.assertRaises(SystemExit) as exit_handler:
            test = ZacSchimpf3.Main(invalid_values)
        self.assertEqual(exit_handler.exception.code, "Valid operator names (add, subtract, multiply, divide)")

    def test_main_fail_invalid_numeric_values(self):
        invalid_values = [["add", "invalid", '1'], ["add", '0', 'invalid']]

        for current_values in invalid_values:
            with self.assertRaises(SystemExit) as exit_handler:
                test = ZacSchimpf3.Main(current_values)
            self.assertEqual(exit_handler.exception.code, "Failed to convert input to numeric values")

    def test_main_ok_input_conversion(self):
        standard_values = [["add", '-2', '-1'],
                           ["subtract", '0', '2'],
                           ["multiply", '0', '3'],
                           ["divide", '0', '4']]
        return_values = [["add", -2, -1],
                         ["subtract", 0, 2],
                         ["multiply", 0, 3],
                         ["divide", 0, 4]]

        index = 0
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_input_raw() == return_values[index], "Failed to validate input conversion")
            index += 1

    def test_main_ok_output_format(self):
        standard_values = ["add", '-2', '-3']

        index = 0
        output = "Answer = -5.00"

        test = ZacSchimpf3.Main(standard_values)
        self.assertTrue(test.get_output() == output, "Failed to validate input results")
        index += 1

    def test_main_ok_py_file_trim(self):
        standard_values = [["c:\\users\\name\\documents\\test.file", "add", '-1', '-2'],
                           ["/home/name/documents/test.file", "add", '-2', '-2'],
                           ["JaneDoe3.py", "add", '-3', '-2']]
        return_values = [-3.0, -4.0, -5.0]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate directory trim")
            index += 1

    def test_main_ok_results_many_values(self):
        standard_values = [["add", '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', "-10"],
                           ["subtract", "100", '9', '8', '7', '6', '5', '4', '3', '2', '1'],
                           ["multiply", '2', '3', '4', '5', '6', '7', '8', '9', "10", "11"],
                           ["divide", '39916800', '10', '9', '8', '7', '6', '5', '4', '3', '2']]
        return_values = [-55, 55, 39916800, 11]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_ok_results_random_negative(self):
        standard_values = [["add", str(random.random() * -1), str(random.random() * -1)],
                           ["multiply", str(random.random() * -1), str(random.random())],
                           ["divide", str(random.random() * -1), str(random.random())]]

        summation = float(standard_values[0][1]) + float(standard_values[0][2])
        product = float(standard_values[1][1]) * float(standard_values[1][2])
        quotient = float(standard_values[2][1]) / float(standard_values[2][2])
        return_values = [summation, product, quotient]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate random negative result")
            index += 1

    def test_main_ok_results_random_positive(self):
        standard_values = [["subtract", str(random.random()), str(random.random())],
                           ["multiply", str(random.random()), str(random.random())],
                           ["divide", str(random.random()), str(random.random())]]

        difference = float(standard_values[0][1]) - float(standard_values[0][2])
        product = float(standard_values[1][1]) * float(standard_values[1][2])
        quotient = float(standard_values[2][1]) / float(standard_values[2][2])
        return_values = [difference, product, quotient]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate positive random result")
            index += 1

    def test_main_ok_lab_sample_addition(self):
        values = [["add", '1', '2'],
                  ["add", '1', '2', "-3.5"],
                  ["add", '-1', '2', "-3.5"]]

        return_values = [0, -3.5, -4.5]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_ok_lab_sample_division(self):
        values = [["divide", '0', '1.5'],
                  ["divide", '-1', '1.5'],
                  ["divide", '-1', '-1.5']]

        return_values = [0, -0.67, 0.67]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_ok_lab_sample_multiplication(self):
        values = [["multiply", '0', '0'],
                  ["multiply", '0', '2.5'],
                  ["multiply", '0', '2.5', '-1'],
                  ["multiply", '0', '2.5', '-1', '-1']]

        return_values = [0, 2.5, -2.5, 2.5]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_ok_lab_sample_subtraction(self):
        values = [["subtract", '-1', '-2'],
                  ["subtract", '-1', '2'],
                  ["subtract", '-1', '2', '-2', '1.5']]

        return_values = [0, 2, 0.5]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_ok_two_values(self):
        standard_values = [["add", '-2', '-3'],
                           ["subtract", '4', '3'],
                           ["multiply", '2', '5'],
                           ["divide", '6', '2']]
        return_values = [-5.0, 1.0, 10.0, 3.0]

        index = 0
        output = "Answer = {:.2f}"
        for current_list in standard_values:
            test = ZacSchimpf3.Main(current_list)
            self.assertTrue(test.get_output() == output.format(return_values[index]),
                            "Failed to validate input results")
            index += 1

    def test_main_fail_input_no_value(self):
        invalid_values = []

        with self.assertRaises(SystemExit) as exit_handler:
            test = ZacSchimpf3.Main(invalid_values)
        self.assertEqual(exit_handler.exception.code, "Need to provide operator")

    def test_main_fail_input_one_value(self):
        invalid_values = ["add"]

        with self.assertRaises(SystemExit) as exit_handler:
            test = ZacSchimpf3.Main(invalid_values)
        self.assertEqual(exit_handler.exception.code, "Need to provide at least two values")

    def test_main_fail_input_two_values(self):
        invalid_values = ["add", '0']

        with self.assertRaises(SystemExit) as exit_handler:
            test = ZacSchimpf3.Main(invalid_values)
        self.assertEqual(exit_handler.exception.code, "Need to provide at least two values")


if __name__ == '__main__':
    unittest.main()
