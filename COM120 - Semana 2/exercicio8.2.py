"""
Exercicio 8.2 do livro:
Comece definindo a classe Teste e depois criando duas instâncias de Teste
"""


class Teste:
    def __init__(self, versao: object = 1.02):
        self.versao = versao


a = Teste()
print(f'Versão de A: {a.versao}')
b = Teste()
print(f'Versão de B: {b.versao}')
Teste.versao = 1.03
print(f'Versão de teste atualizada para: {Teste.versao}')
print(f'Versão de A: {a.versao}')
print(f'Versão de B: {b.versao}')
# print(f'Versão Ponto: {Ponto.versao}')
# NameError: name 'Ponto' is not defined
a.versao = 'Última!'
print(f'Versão de A: {a.versao}')
print(f'Versão de B: {b.versao}')
