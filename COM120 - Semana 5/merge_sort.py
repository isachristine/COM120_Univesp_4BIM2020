

def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)
        print(f'Ordenando... {v}')


def intercala(v, ini, meio, fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    L.append(999)  # sentinela
    R.append(999)  # sentinela
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1


lista = [5, 2, 4, 7, 1, 3, 2]
print(f'Lista inicial: {lista}')
merge_sort(lista, 0, len(lista)-1)
