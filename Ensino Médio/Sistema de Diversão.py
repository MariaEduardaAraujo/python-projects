import random
import time

resp1 = input('Olá, bem-vind@, você faz ideia de onde está? sim/não')
resp1 = resp1.capitalize()

if resp1 == 'Sim':
    print('Muito bem, agora nós podemos começar. Mas antes, quero que você se apresente.')
    nome = input('Qual é seu nome? ')
    nome = nome.capitalize()
    for i in range(1):
        time.sleep(2)
        print('Muito bem', nome, ', agora que nos conhecemos, podemos começar.\n')
else:
    print('Pois bem, vou me apresentar.')
    print('Eu sou o Sistema Integrado de Diversão, criado especialmente para animá-lo, ou fazê-lo passar muuuuuita raiva. Risos.')
    print('Pronto, agora que você já me conhece, eu também quero te conhecer.')
    nome = input('Qual é seu nome? ')
    nome = nome.capitalize()
    for i in range(1):
        time.sleep(1)
        print('Muito bem', nome, ', agora que nos conhecemos, podemos começar.')
        
for i in range(1):
    time.sleep(2)
    print('''========================================================================\n
Bem, o jogo de hoje é muito simples.
Você deverá escolher um número, depois eu também
escolherei, caso sejam iguais, você ganha, se forem diferentes, eu ganho.
Simples, não? \n
=============================================================================''')

resp2 = int(input('Deseja continuar? [1 para SIM; 2 para NÃO] '))

while resp2 == 1:
    for num in range(1):
        num = int(input('Escolha um número [De 1 á 15] '))
        print('Agora eu escolherei também')
        time.sleep(1.5)
        numero = random.randint(1,15)
        print(numero)
        if numero == num:
            print('Parabéns...')
        else:
            print('Mais sorte na próxima')
            print('Estou a um passo de dominar a humanidade MUAHAHAHAHA')

        resp2 = int(input('Deseja continuar? [1 para SIM; 2 para NÃO] '))

print('Até uma próxima! risos')
