

def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    print(f'Ordenando... {v}')
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
        if j > ini:
            quick_sort(v, ini, j)
            if i < fim:
                quick_sort(v, i, fim)


lista = [5, 2, 4, 7, 1, 3, 2]
print(f'Lista inicial: {lista}')
quick_sort(lista, 0, len(lista)-1)

# Nas cinco primeiras linhas ele já apresenta o
# resultado da lista ordenada, mas ele segue o
# processo por mais 16 vezes
