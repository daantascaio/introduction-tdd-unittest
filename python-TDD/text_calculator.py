from calculator import sum
import unittest


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    unittest.main()
