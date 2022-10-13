import unittest
from numero_decimal import romano_a_decimal

class PrimerTest(unittest.TestCase):
    def test_1(self):
        resultado = romano_a_decimal("I")
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = romano_a_decimal("II")
        self.assertEqual(resultado, 2)