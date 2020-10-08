

def stringCount(filename, target):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(f'A palavra {target} aparece {wordList.count(target)} vezes.')


stringCount('example4.3.txt', 'this')
stringCount('example4.3.txt', 'the')
stringCount('example4.3.txt', 'line')
