import random

print("Tente acertar o número secreto")
numeroSecreto = random.randint(1,20)
i = 0

while (i == 0):
    palpite = int(input("Digite um número de 1 a 20: "))
    if (palpite == numeroSecreto):
        print("Acertou")
        i = i + 1
        break
    elif (palpite != numeroSecreto):
            if (palpite < numeroSecreto):
                print("O número secreto é maior")
            else:
                print("O número secreto é menor")
    else: 
         print("Erro")
print(" ")