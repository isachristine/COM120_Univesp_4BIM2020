

def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                print(f'Ordenando... {v}')


lista = [5, 2, 4, 7, 1, 3, 2]
print(f'Lista inicial: {lista}')
print(bubble_sort(lista))
