# Exercício 8.9 do livro
# Reimplemente o método dequeue() da classe Queue de modo que
# seja levantada uma exceção KeyboardInterrupt (um tipo de exceção
# impróprio, nesse caso) com a mensagem 'remoção de uma fila
# vazia ' (uma mensagem de erro realmente apropriada) se for feita
# uma tentativa de remover algum elemento de uma fila vazia.
#
# >>> queue = Queue()
# >>> queue.dequeue()
#
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     queue.dequeue()
#   File "/Users/me/ch8.py", line 183, in dequeue
#     raise KeyboardInterrupt('remoção de uma fila vazia')
# KeyboardInterrupt: remoção de uma fila vazia

