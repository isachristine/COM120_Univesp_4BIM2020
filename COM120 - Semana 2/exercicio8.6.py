# Exercício 8.6 do livro
# Implemente operadores sobrecarregados repr() e == para a classe Carta.
# Sua nova classe Carta deverá se comportar como a seguir:
#
# >>> Carta('3', '♠') == Carta('3', '♠')
# True
# >>> Carta('3', '♠') == eval(repr(Carta('3', '♠')))
# True
