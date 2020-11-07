import random


def busca_binaria(l, x, ini, fim):
    meio = (ini + fim) // 2

    if fim < ini:
        print(f'O elemento {x} não existe na lista...')
        return -1

    if x == l[meio]:
        print(f'O elemento {x} está na posição {meio}')

    if x < l[meio]:
        busca_binaria(l, x, ini, meio - 1)

    if x > l[meio]:
        busca_binaria(l, x, meio + 1, fim)


lista = random.sample(range(100), 20)
print(f'Lista desordenada: {lista}')
lista.sort()
print(f'Lista ordenada: {lista}')
print(busca_binaria(lista, 15, 0, len(lista)-1))

