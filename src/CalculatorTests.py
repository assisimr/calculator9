import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)


    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)


    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(4, 2), 8)
        self.assertEqual(self.calculator.result, 8)


    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)


    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(3), 9)
        self.assertEqual(self.calculator.result, 9)


    def test_square_root_method_calculator(self):
        test_data = CsvReader('/src/square_root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(row['Value']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
