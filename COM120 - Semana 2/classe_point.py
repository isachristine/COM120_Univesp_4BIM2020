# O parâmetro self é usado para referenciar o objeto posteriormente.
# Ao criamos um objeto da classe Point, poderemos usar a função setx
# por exemplo, apenas chamando o nome dele + . + função: ex: objeto.setx

class Point:
    def __init__(self, x: object = 0, y: object = 0):
        # a função init vai ser instanciada ao criar um objeto.
        # a função init guarda os atributos da classe.
        # colocamos um valor para x e y caso o user não informe.
        self.x = x
        self.y = y

    def setx(self, x):
        self = x

    def sety(self, y):
        self = y

    def ge(self):
        # essa função permite que o user pegue os valores
        # de x e y, caso ele queira.
        return self.x, self.y

    def move(self, offsetx, offsety):
        # essa função pegará o valor de x e y novos e vai
        # somar com o valor anterior, gravado em offset
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        # quando imprimimos o objeto, ele vai mostrar
        # o conteúdo que estiver aqui.
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
        # outra forma de escrever esse return é:
        # return '({},{})'.format(self.x, self.y)

    def __add__(self, other):
        # se for um objeto da classe point, o other será
        # somado como x + x e y + y
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            # se o other for uma constante:
            return Point(self.x + other, self.y + other)

    def getx(self):
        """
        Exercício 8.1 do livro:
        Acrescente o método getx() à classe Ponto; esse método não aceita entrada
        e retorna a coordenada x do objeto Ponto que chama o método.
        """
        return self.x






p = Point()
print(f'P está em: {p}')
p.move(3, -5)
print(f'P foi para: {p}')
q = Point(3, 4)
print(f'Q está em: {q}')
q.move(9, -3)
print(f'Q foi para: {q}')
print(f'O valor da soma dos pontos P {p} e Q {q} resulta os pontos: {p+q}')
print(f'Se somarmos 5 no nosso P, de {p} ele vai ser {p+5}')
print(f'O valor de x no ponto P é {p.getx()}')
