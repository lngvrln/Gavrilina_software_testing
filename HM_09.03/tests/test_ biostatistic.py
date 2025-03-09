import unittest
from calc_code.biostatistic import Calculation_Biostatistic

class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculation_Biostatistic()

    def test_add(self):
        a, b = 5, 3
        expected_result = 8

        result = self.calc.add(a, b)

        self.assertEqual(result, expected_result)

    def test_subtract(self):
        a, b = 5, 3
        expected_result = 2

        result = self.calc.subtract(a, b)

        self.assertEqual(result, expected_result)

    def test_multiply(self):
        a, b = 5, 3
        expected_result = 15

        result = self.calc.multiply(a, b)

        self.assertEqual(result, expected_result)

    def test_divide(self):
        a, b = 6, 3
        expected_result = 2

        result = self.calc.divide(a, b)

        self.assertEqual(result, expected_result)

    def test_divide_by_zero(self):
        a, b = 6, 0

        with self.assertRaises(ValueError):
            self.calc.divide(a, b)

if __name__ == '__main__':
    unittest.main()