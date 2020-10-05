# Arquivo "example.txt" inicialmente:
# Ola classe!
# Aqui eh a aula 2
# Sobre arquivos


def readFile(filename):
    infile = open(filename, 'r') # Abre arquivo recebido pela func, para leit
    content = infile.read() # Lê o arquivo e salva na var content
    infile.close() # Fecha o arquivo
    wordList = content.split() # cria uma lista e insere o content, com split
    print(wordList) # imprime a lista
    return len(wordList), len(content) # retorna o tamanho da var wordList e content


def writeFile(insertText):
    outfile = open('example.txt', 'w')  # Abre em modo de escrita
    outfile.write(insertText)  # Escreve por cima do arquivo


n_words, n_chars = readFile('example.txt')
# solicita núm de palavras e caracteres do texto 'example.txt', via func readFile
print(f'O texto possui {n_chars} caracteres e {n_words} palavras.')


novoTexto = writeFile(str(input('Informe o novo texto desejado: ')))
n_words, n_chars = readFile('example.txt')
print(f'O texto possui {n_chars} caracteres e {n_words} palavras.')