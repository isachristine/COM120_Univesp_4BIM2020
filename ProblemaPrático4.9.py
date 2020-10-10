

def meuGrep(filename, target):
    """
    :param filename: caminho para o arquivo (string)
    :param target: palavra procurada na linha (string)
    :return: linhas em que a palavra procurada aparece.
    """
    infile = open(filename, 'r')
    for line in infile:
        if target in line:
            print(line, end='')
    infile.close()


meuGrep('example4.3.txt', 'line')
print('\n')
meuGrep('example4.3.txt', 'the')
print('\n')
meuGrep('example4.3.txt', 'above')
