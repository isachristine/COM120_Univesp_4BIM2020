

def fatorial(n):
    if n == 0:
        return 1
    else:
        res = n * fatorial(n - 1)
        return res


print(fatorial(4))
