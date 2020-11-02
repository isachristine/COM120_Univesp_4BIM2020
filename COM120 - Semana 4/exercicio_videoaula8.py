# Implementar um programa de gerenciamento
# de duas filas em um banco: prioritária e
# normal.
# Seu programa deverá permitir que pessoas
# sejam inseridas no fim de cada fila,
# dependendo da idade de cada uma (acima de
# 60 anos entra na fila prioritária).
# A saída de pessoas da fila deve ocorrer da
# seguinte forma: a cada duas pessoas que
# saem da fila prioritária, uma sai da fila normal.


class FilaBanco():
    def __init__(self):
        self.data_preferencial = []
        self.data_comum = []

    def inserir(self, x):
        if x > 60:
            self.data_preferencial.append(x)
        else:
            self.data_comum.append(x)

    def atender(self):
        while len(self.data_comum) > 0:
            if len(self.data_preferencial) >= 2:
                print(f'Por favor, dirija-se ao balcão: {self.data_preferencial.pop(0)}')
                print(f'Por favor, dirija-se ao balcão: {self.data_preferencial.pop(0)}')
                print(self.data_preferencial)
                print(f'Por favor, dirija-se ao balcão: {self.data_comum.pop(0)}')
                print(self.data_comum)
            elif len(self.data_preferencial) >= 1:
                print(f'Por favor, dirija-se ao balcão: {self.data_preferencial.pop(0)}')
                print(self.data_preferencial)
                print(f'Por favor, dirija-se ao balcão: {self.data_comum.pop(0)}')
                print(self.data_comum)
            else:
                print(f'Por favor, dirija-se ao balcão: {self.data_comum.pop(0)}')
                print(self.data_comum)
        print('Atendimentos do dia: encerrados.')


filaComum = FilaBanco()
filaComum.inserir(65)
filaComum.inserir(35)
filaComum.inserir(63)
filaComum.inserir(45)
filaComum.inserir(72)
filaComum.inserir(25)
filaComum.inserir(78)
filaComum.inserir(27)
filaComum.inserir(39)
filaComum.inserir(48)
filaComum.inserir(59)
filaComum.inserir(55)
print(f'Fila de atendimento comum: {filaComum.data_comum}')
print(f'Fila de atendimento preferencial: {filaComum.data_preferencial}')
filaComum.atender()
