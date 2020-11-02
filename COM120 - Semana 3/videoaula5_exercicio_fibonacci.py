import time
# Implementar uma função recursiva para
# calcular o n-ésimo termo da sequência de
# Fibonacci.
# Considere os três pontos definidos para o
# problema:
# 1) f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) p/ n>=2
# 2) n=0 ou n=1
# 3) n deve ser decrementado a cada chamada


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# Código copiado da vídeo aula do professor.
# Verificado que essa versão recursiva demora mais pra obter
# a resposta, do que se usar a versão interativa apresentada
# abaixo.


def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res


# Versão com MEMOIZAÇÃO
m = dict()
# Cria um vetor para armazenar as informações da função recursiva


def fib_me(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        # Se a variável for diferente de None, é porque já existe no
        # vetor m criado, então vai pegar aquele valor da "memória"
        return m[n]
    else:
        m[n] = fib_me(n - 1) + fib_me(n - 2)
        # Se não existir, vai executar a função recursiva, mas com
        # a memoização, então ficará mais rápido que a recursiva.
        # O valor recbido é armazenado no vetor m.
        return m[n]


n = 3
start = time.time()
print(fib_it(n))
print(f'Interativo: {time.time() - start}')
start = time.time()
print(fib_rec(n))
print(f'Recursivo: {time.time() - start}')
start = time.time()
print(fib_me(n))
print(f'Memoização: {time.time() - start}')
