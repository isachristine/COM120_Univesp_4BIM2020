

def stringCount(filename, target):
    """
    Essa função recebe como parâmetros um caminho de arquivo
    em formato string e uma string denominada "target", que será
    procurada dentro do arquivo. Como retorno vai mostrar quantas
    vezes a palavra inserida no parâmetro "target" se repete no
    texto.
    """
    infile = open(filename, 'r')
    # Abre o arquivo em modo leitura
    content = infile.read()
    # Puxa o conteúdo lido para dentro da variável content
    infile.close()
    # Fecha o arquivo
    wordList = content.split()
    # Cria uma lista que recebe e separa os itens da variável content
    print(f'A palavra {target} aparece {wordList.count(target)} vezes.')
    # Contagem da palavra passada no parâmetro target, dentro da lista


stringCount('example4.3.txt', 'this')
stringCount('example4.3.txt', 'the')
stringCount('example4.3.txt', 'line')
