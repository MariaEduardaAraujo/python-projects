import random
import time

itens = ['Pedra', 'Papel', 'Tesoura']
j = 0
v = 0
em = 0

print('Olá, você está no Sistema de Diversão, agora, um sitema novo e melhorado, pronto para atendê-lo')

for i in range(1):
    time.sleep(1)
    print('==='*23)
    time.sleep(2)
    print('O jogo de hoje é o velho Pedra, Papel e Tesoura')

print('Para jogar você só precisa saber de algumas coisas: \n')

print('>>> Tesoura corta Papel')
print('>>> Papel cobre Pedra')
print('>>> Pedra quebra Tesoura \n')

try:
    perg1 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))
except:
    print('Opção inválida')
    print('Tente novamente')
    perg1 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))

while perg1 == 1:
    j += 1
    for comp in range(1):
        perg2 = input('Sua escolha: ')
        perg2 = perg2.capitalize()

        print('Sua escolha foi', perg2)
        comp = random.choice(itens)

        if perg2 == 'Pedra' and  comp == 'Papel':
            print('Eu escolhi: ', comp)
            print('Eu ganhei!!!')

        elif perg2 == 'Papel' and comp == 'Tesoura':
            print('Eu escolhi: ', comp)
            print('Eu ganhei!!!')
            
        elif perg2 == 'Tesoura' and comp == 'Pedra':
            print('Eu escolhi: ', comp)
            print('Eu ganhei!!!')

        elif perg2 == comp:
            print('Empate, eu escolhi', comp)
            em += 1
        elif perg2 != itens:
            print('INVÁLIDO')
        else:
            print('Você ganhou')
            v += 1
            print('Eu escolhi', comp)
                
        perg1 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))

print('Até mais, foi um bom jogo!!')
print('Placar final    Partidas jogadas    Partidas vencidas     Empates')
print('XXXXXXXXXXXX         ',j,'                   ',v ,'              ', em)

#Há um bug neste código e em certos momentos aparece a opção "INVÁLIDO", mesmo que tudo esteja correto
