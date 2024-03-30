import random;

numSecreto = random.randint(1,100)
i = 5

while (i != 0):
    palpite =int(input("Digite um número (1 a 100): "))
    i = i - 1

    if (palpite == numSecreto):
        print("Acertou")
        break
    elif (palpite != numSecreto):
        if (palpite > numSecreto):
            print("Tente novamente, o número secreto é menor")
        else:
            print("Tente novamente, o número secreto é maior")
    else:
        print("Erro")
