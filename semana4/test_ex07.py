import unittest
from exercicio07 import calculo_porcentagem_entre_0_e_100

class CalculoPorcentagemTeste(unittest.TestCase):
    def test_calculo_porcentagem_cenario_1(self):
        self.assertEqual(64, calculo_porcentagem_entre_0_e_100(80, 80))
        self.assertNotEqual(50, calculo_porcentagem_entre_0_e_100(72, 87))

    def test_calculo_porcentagem_cenario_2(self):
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_100(2,-1)

if __name__ == '__main__':
    unittest.main()
