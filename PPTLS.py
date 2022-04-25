import random
import time

itens = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

print('Olá, você está novamente no Sistema de Diversão, agora, um sitema novo')
print('e melhorado, pronto para atendê-lo')

for i in range(1):
    time.sleep(1)
    print('==='*23)
    time.sleep(2)

print('Para jogar você só precisa saber de algumas coisas: \n')

print('>>> Tesoura corta Papel')
print('>>> Papel cobre Pedra')
print('>>> Pedra esmaga Lagarto')
print('>>> Lagarto envenena Spock')
print('>>> Spock quebra Tesoura')
print('>>> Tesoura decapita Largato')
print('>>> Lagarto come Papel')
print('>>> Papel refuta Lagarto')
print('>>> Spock vaporiza Pedra')
print('>>> Pedra quebra Tesoura \n')
try:
    perg2 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))
except:
    print('Opção inválida')
    print('Tente novamente')
    perg2 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))

while perg2 == 1:
    for comp in range(1):
        perg3 = input('Sua escolha: ')
        perg3 = perg3.capitalize()
        comp = random.choice(itens)
        
        if perg3 == 'Pedra' and  comp == 'Papel':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Papel' and comp == 'Tesoura':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)
            
        elif perg3 == 'Tesoura' and comp == 'Pedra':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Lagarto' and comp == 'Pedra':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Spock' and comp == 'Lagarto':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Tesoura' and comp == 'Spock':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Lagarto' and comp == 'Tesoura':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Papel' and comp == 'Lagarto':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Lagarto' and comp == 'Papel':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == 'Pedra' and comp == 'Spock':
            print('Eu ganhei!!!')
            print('Eu escolhi: ', comp)

        elif perg3 == comp:
            print('Empate, eu escolhi', comp)

        elif perg3 != comp:
            print('Parabéns, você venceu!!')
            print('Eu escolhi: ', comp)
        elif perg3 != itens:
            print('Opção inválida')
            quit()  
        perg2 = int(input('Deseja prosseguir [1 para SIM; 2 para NÃO] '))
print('Até mais!!')
