"""
Considere uma entidade Funcionário, que possui
nome, data de admissão e salário. Implemente sua
classe, definindo também alguns métodos para
manipulação dos atributos.
Em seguida, considere a entidade Gerente, que
também é um funcionário. Além dos atributos de
funcionário, um gerente também contém um
bônus, que é uma porcentagem adicional aplicada
no seu salário.
Implemente a classe Gerente como uma extensão
de Funcionário.
"""


class Employee:
    def __init__(self, name: object, admissionDate: object, salary: object) -> object:
        self.name = name
        self.admissionDate = admissionDate
        self.salary = salary

    def increaseSalary(self, increase):
        self.salary += (self.salary * increase) / 100

    def changeName(self, surname):
        self.name += surname

    def __repr__(self):
        return 'Nome: {} \nData da admissão: {} \nSalário R$ {:.2f}'\
            .format(self.name, self.admissionDate, self.salary)


func1 = Employee('Vanessa Caroline ', '20/09/2017', 1500)
print(func1)
print(' ')
print('Atualização do nome do(a) funcionário(a), após casamento:')
func1.changeName('Rodrigues')
print(func1)
print(' ')
print('Atualização do salário do(a) funcionário(a), após dissídio de 9%:')
func1.increaseSalary(9)
print(func1)


class Manager(Employee):
    def bonusSalary(self, bonusPercentage):
        return ((self.salary * bonusPercentage) / 100) + self.salary


geren1 = Manager(name='Giovana Clemente ',
                 admissionDate='08/03/2015',
                 salary=2350,
                 )

print('--------------------------------------------------------------')
print(geren1)
print(' ')
print('Atualização do nome do(a) gerente, após casamento:')
geren1.changeName('Pereira')
print(geren1)
print(' ')
print(f'Valor do salário do(a) gerente, com o bônus: {geren1.bonusSalary(6):.2f}')
print(' ')
print('Atualização do salário do(a) gerente, após dissídio de 9%:')
geren1.increaseSalary(9)
print(geren1)
print(' ')
print(f'Valor do salário do(a) gerente, com o bônus: {geren1.bonusSalary(6):.2f}')

