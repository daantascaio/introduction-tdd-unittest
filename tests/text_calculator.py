try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

from calculator import sum
import unittest


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 10, 15),
            (-2, 10, 8),
            (10.5, 10.5, 21),
            (10.5, -10, 0.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(sum(x, y), saida)

    def test_sum_x__nao_e_int_ou_float_deve_retornar_assertionError(self):
        with self.assertRaises(AssertionError):
            sum('11', 0)

    def test_sum_y__nao_e_int_ou_float_deve_retornar_assertionError(self):
        with self.assertRaises(AssertionError):
            sum('11', 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
