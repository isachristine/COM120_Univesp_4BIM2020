from func import soma, multi


def testeSoma():
    assert soma([1, 2, 3]) == 6, "Deve ser 6"


def testeMulti():
    assert multi((2, 3, 4)) == 24, "Deve ser 24"


if __name__ == "__main__":
    testeSoma()
    testeMulti()
    print('Tudo ok!')


# Nesse modelo, ao encontrar o erro na soma, o teste não vai
# verificar a próxima, que é a multi

