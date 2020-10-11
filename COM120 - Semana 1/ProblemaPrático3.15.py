# O exercício agora pede que use o que aprendemos na página 84,
# para desenhar o símbolo das olimpíadas
import turtle

# Acredito que isso abra a tela
s = turtle.Screen()
t = turtle.Turtle()


# A tartaruga, acredito eu, é o que vai desenhar...
def jump(t, x, y):
    # Coloca a caneta para desenhar
    t.penup()
    # Manda a caneta para os pontos x, y
    t.goto(x, y)
    # 'Tampa' a caneta
    t.pendown()


def olimpiadas(t, x, y):
    # define direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)
    # move para (x, y) e desenha um círculo
    jump(t, x, y)
    t.circle(100)


olimpiadas(t, -300, 100)
# Primeiro círculo começa à esquerda, o 100 acredito
# ser a altura
olimpiadas(t, -75, 100)
# Mantive a altura 100 e somei 225 em relação a posição
olimpiadas(t, 150, 100)
# Somei mais 250 para a última posição.
olimpiadas(t, -187.5, 0)
# Mudei a altura para 0, o que fez com que pulasse para
# baixo pela metade. Somei a posição do primeiro e do
# segundo círculo (-300 - 75 = -375) e dividi por dois
olimpiadas(t, 37.5, 0)
# Mantive a altura e somei 225 para a posição do último
# círculo
