def romano_a_decimal(numeroRomano):
    
    decimal = 0

    for letra in numeroRomano:
        if letra == "I":
            decimal += 1
        if letra == "X":
            decimal += 10
        if letra == "V":
            decimal += 5
        if letra == "IV":
            decimal += 4
            
    return decimal

##############################################test#####################################################

import unittest

class PrimerTest(unittest.TestCase):
    def test_1(self):
        resultado = romano_a_decimal("I")
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = romano_a_decimal("II")
        self.assertEqual(resultado, 2)
    def test_3(self):
        resultado = romano_a_decimal("III")
        self.assertEqual(resultado, 3)
    def test_10(self):
        resultado = romano_a_decimal("X")
        self.assertEqual(resultado, 10)
    def test_5(self):
        resultado = romano_a_decimal("V")
        self.assertEqual(resultado, 5)
    def test_4(self):
        resultado = romano_a_decimal("X")
        self.assertEqual(resultado, 10)

if __name__ == "__main__":
    unittest.main()