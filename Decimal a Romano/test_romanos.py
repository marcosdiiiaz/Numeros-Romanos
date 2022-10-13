import unittest
from numeros_romanos import decimal_a_romano

class PrimerTest(unittest.TestCase):
    def test_1(self):
        resultado = decimal_a_romano(1)
        self.assertEqual(resultado, "I")
    def test_2(self):
        resultado = decimal_a_romano(2)
        self.assertEqual(resultado, "II")
    def test_4(self):
        resultado = decimal_a_romano(4)
        self.assertEqual(resultado, "IV")
    def test_6(self):
        resultado = decimal_a_romano(5)
        self.assertEqual(resultado, "V")
    def test_7(self):
        resultado = decimal_a_romano(6)
        self.assertEqual(resultado, "VI")
    
    #def test_7(self):
        #resultado = decimal_a_romano(9)
        #self.assertEqual(resultado, "IX")
    #def test_8(self):
        #resultado = decimal_a_romano(10)
        #self.assertEqual(resultado, "X")
       
if __name__ == "__main__":
    unittest.main()
    
