import random

# Como o professor explicou, já existe a classe list, mas ela
# não possui a função choice, então fizemos a classe MyList
# usando a herança da classe list


class MyList(list):

    def choice(self):
        """"
        A função choice vai pegar um objeto da classe MyList
        e vai sortear um valor dentro dele.
        :return: valor aleatório do objeto da classe MyList
        """
        return random.choice(self)


l = MyList([1, 3, 15, 27])
print(f'Da lista {l}, o valor aleatório é {l.choice()}')

