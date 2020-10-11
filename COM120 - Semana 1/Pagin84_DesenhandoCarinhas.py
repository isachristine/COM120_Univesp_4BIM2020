# Copiei o código do livro para ter de referência
import turtle

s = turtle.Screen()
t = turtle.Turtle()


def jump(t, x, y):
    'faz tartaruga saltar para coordenadas (x, y)'
    t.penup()
    t.goto(x, y)
    t.pendown()


def emoticon(t, x, y):
    'tartaruga t desenha uma carinha com queixo na coordenada (x, y)'
    # define direção da tartaruga e tamanho da caneta
    t.pensize(3)
    t.setheading(0)
    # move para (x, y) e desenha cabeça
    jump(t, x, y)
    t.circle(100)
    # desenha olho direito
    jump(t, x + 35, y + 120)
    t.dot(25)
    # desenha olho esquerdo
    jump(t, x - 35, y + 120)
    t.dot(25)
    # desenha sorriso
    jump(t, x - 60.62, y + 65)
    t.setheading(-60)
    t.circle(70, 120)


emoticon(t, -100, 100)
emoticon(t, 150, 100)
