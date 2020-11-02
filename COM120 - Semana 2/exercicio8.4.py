# Exercício 8.4 do livro:
# Modifique a classe Animal que desenvolvemos na seção anterior de modo
# que aceite um construtor com dois, um ou nenhum argumento de entrada:
# Copiada classe do livro.
#
# Observação: pelo "RUN" ele vai imprimir "NONE" após cada impressão de
# fala dos objetos criados. Pelo Python Console não, só a fala.


class Animal:
    # representa um animal
    def __init__(self, especie='animal', linguagem='emitir sons'):
        self.esp = especie
        self.ling = linguagem

    def setEspecie(self, especie):
        # define a especie do animal
        self.esp = especie

    def setLinguagem(self, linguagem):
        # define a linguagem do animal
        self.ling = linguagem

    def fala(self):
        # exibe uma sentença pelo animal
        print(f'Eu sou um {self.esp} e eu sei {self.ling}')


snoopy = Animal('cão', 'latir')
print(snoopy.fala())
tweety = Animal('canário')
print(tweety.fala())
animal = Animal()
print(animal.fala())
