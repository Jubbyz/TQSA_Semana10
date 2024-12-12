import unittest
from numeroromano import converte

class TesteConversorRomano(unittest.TestCase):

    def test_conversoes_validas(self):
        """
        Testa conversões de números romanos válidos.
        """
        self.assertEqual(converte('I'), 1)
        self.assertEqual(converte('V'), 5)
        self.assertEqual(converte('II'), 2)
        self.assertEqual(converte('XXII'), 22)
        self.assertEqual(converte('IX'), 9)
        self.assertEqual(converte('XXIV'), 24)

    def test_conversoes_invalidas(self):

       # Testa entradas inválidas ou que são contra as regras

        with self.assertRaises(ValueError):
            converte('IIII')

        with self.assertRaises(ValueError):
            converte('VV')

        with self.assertRaises(ValueError):
            converte('A')

if __name__ == "__main__":
    unittest.main()