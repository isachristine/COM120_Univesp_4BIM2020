# Exercício 8.3 do livro:
# Implemente a classe Retângulo, que representa retângulos.
# A classe deverá implementar estes métodos:
#
# •setTamanho(largura, comprimento): aceita dois valores numéricos
# como entrada e define o comprimento e largura do retângulo.
#
# •perímetro(): retorna o perímetro do retângulo.
#
# •área(): retorna a área do retângulo.


class Retangulo:
    def __init__(self, largura: object = 0, comprimento: object = 0):
        self.largura = largura
        self.comprimento = comprimento

    def __repr__(self):
        return '({}, {})'.format(self.largura, self.comprimento)

    def setTamanho(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def perimetro(self):
        largTotal = self.largura * 2
        compTotal = self.comprimento * 2
        return largTotal + compTotal

    def area(self):
        return self.largura * self.comprimento


retang1 = Retangulo(3, 4)
print(f'Medidas do retângulo: {retang1}')
print(f'O perímetro do retângulo é: {retang1.perimetro()}')
print(f'A área do retângulo é: {retang1.area()}')

