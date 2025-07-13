"""
O arquivo contém testes unitários para as funções do 

arquivo calculadora.py usando o módulo unittest.
"""
import unittest
from calculadora import soma, subt, mult, div

class TestCalculadora(unittest.TestCase):
    """Testes para as funções da  calculadora."""
    def test_soma(self):
        """Teste de soma com caso de erro."""
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(2.5, 0.5), 3.0)
        with self.assertRaises(TypeError):
            soma(2, "a")

    def test_subt(self):
        """Teste de subtração com caso de erro."""
        self.assertEqual(subt(5, 2), 3)
        self.assertEqual(subt(-1, -1), 0)
        self.assertEqual(subt(2.5, 0.5), 2.0)
        with self.assertRaises(TypeError):
            subt("b", 1)

    def test_mult(self):
        """Teste de multiplicação com caso de erro."""
        self.assertEqual(mult(4, 3), 12)
        self.assertEqual(mult(-1, 1), -1)
        self.assertEqual(mult(2.5, 2), 5.0)
        with self.assertRaises(TypeError):
            mult(2, None)

    def test_div(self):
        """Teste de divisão com caso de erro."""
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-4, 2), -2)
        self.assertEqual(div(5.0, 2.5), 2.0)
        with self.assertRaises(TypeError):
            div("x", 2)
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

if __name__ == "__main__":
    unittest.main()
