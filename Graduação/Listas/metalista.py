import random

print('Olá, bem-vind@ ao Mentalista! \n')

numSecreto = random.randint(1,1000)
numTentativas = random.randint(3,10)
chutes = []
cont = 0

print(f"Você tem {numTentativas} tentativas")

while (cont <= numTentativas):
    palpite = int(input('Escolha um número [de 1 á 1000]: '))
    
    if (palpite == numSecreto):
        print('Parabéns... Você acertou!')
        break
    
    elif (palpite < numSecreto):
        print("Tente novamente! O número secreto é maior")
        chutes.append(palpite)
    elif (palpite > numSecreto):
        print("Tente novamente! O número secreto é menor")         
        chutes.append(palpite)
    cont += 1   
    
    if (cont == numTentativas):
        print(f'Mais sorte na próxima. O número secreto era {numSecreto}')
        break

print(f"Você deu os seguintes chutes: {chutes}")