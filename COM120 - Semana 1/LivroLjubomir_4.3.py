infile = open('example4.3.txt')
# O comando acima abre o arquivo
print(infile.read(1))
# O comando acima faz leitura do primeiro caractere
# e para após a leitura. Vai retornar "T"
print(infile.read(5))
# O comando acima faz leitura dos próximos 5 caracteres
# e para após a leitura. Vai retornar "he 3 "
print(infile.readline())
# O comando acima faz leitura da linha, à partir de onde parou.
print(infile.read())
# O comando acima realiza a leitura total, à partir de onde parou.