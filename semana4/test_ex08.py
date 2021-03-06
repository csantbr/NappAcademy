import unittest
from exercicio08 import juros_compostos

class CalculoPorcentagemTeste(unittest.TestCase):
    def test_calculo_porcentagem_cenario_1(self):
        self.assertEqual(119726069573.78, juros_compostos(44520, 40, 44))
        self.assertNotEqual(120000.84, juros_compostos(42000, 10, 2))

    def test_calculo_porcentagem_cenario_2(self):
        with self.assertRaises(TypeError):
            juros_compostos("test", 1, "test")

if __name__ == '__main__':
    unittest.main()
