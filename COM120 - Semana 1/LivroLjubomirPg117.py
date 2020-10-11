# Criando um arquivo do zero

arquivoNovo = open('text.txt', 'w')
print(arquivoNovo.write('Esta é a primeira linha!'))
print(arquivoNovo.write(' Ainda a primeira linha... \n'))
print(arquivoNovo.write('Agora estamos na segunda linha.\n'))
# Para escrever algo que não seja uma string, precisaremos
# primeiro fazer a conversão.
print(arquivoNovo.write('Valor não de string como '+str(5)+' deve ser convertido primeiro.\n'))
print(arquivoNovo.write('Valor não de string como {} deve ser convertido primeiro. \n'.format(5)))
arquivoNovo.close()
