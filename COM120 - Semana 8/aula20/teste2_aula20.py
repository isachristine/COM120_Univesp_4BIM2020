import unittest
from func import soma, multi


class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(soma([1, 2, 3]), 6, "Deve ser 6")

    def test_sum2(self):
        self.assertEqual(multi((2, 3, 4)), 24, "Deve ser 24")


if __name__ == "__main__":
    unittest.main()


# Esse mostra um relatório onde podemos ver o resultado quando há,
# erro, qual foi a(s) função(ões) com erro e também quantas foram
# testadas e quantas falharam. É bem legal!
