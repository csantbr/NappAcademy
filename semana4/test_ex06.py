import unittest
from exercicio06 import calculo_porcentagem_entre_0_e_1

class CalculoPorcentagemTeste(unittest.TestCase):
    def test_calculo_porcentagem_cenario_1(self):
        self.assertEqual(22, calculo_porcentagem_entre_0_e_1(22, 1))
        self.assertNotEqual(20, calculo_porcentagem_entre_0_e_1(16, 1))

    def test_calculo_porcentagem_cenario_2(self):
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_1(2,-1)

if __name__ == '__main__':
    unittest.main()
