import random

print('Olá, bem-vind@ ao Mentalista!')

chutes = []
numSecreto = random.randint(1,1000)
tentativas = random.randint(3,10)
c = 0

print(f"Você tem {tentativas} tentativas")
print()

while (c <= tentativas):
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
    c+=1   
    
    if (c == tentativas):
        print(f'Mais sorte na próxima. O número secreto era {numSecreto}')
        break

print(f"Você deu os seguintes chutes: {chutes}")