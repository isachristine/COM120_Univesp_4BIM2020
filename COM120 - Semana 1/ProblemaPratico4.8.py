

def palavras(filename):
    infile = open(filename, 'r')
    c = 0
    wordList = []
    while c <= 100:
        content = infile.read(1)
        if content != '.':
            wordList.append(content)
        c += 1
    infile.close()
    print(wordList)


'''Eu não consegui fazer esse exercício ainda, então o código
acima está incorreto! O Código acima consegue remover o ponto, mas 
somente se dividir em letras, o que desconfigura as palavras...'''

palavras('example4.3.txt')
