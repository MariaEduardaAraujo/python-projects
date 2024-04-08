'''Criar programa para simular conta bancária, onde terá as seguintes opções: 
1 - Depositar; 
2 - Sacar; 
3 - Saldo 
4 - Sair'''
'''Regras: a) o menu deve ser repetido, e só sair, quando escolher a opção a opção 4; 
b) validar o valor da operação (seja de saque ou depósito que tem que ser maior que 0); 
c) no sacar, tem que validar se tem saldo suficiente (não pode ficar com saldo negativo); 
d) no saldo, deve apresentar "Seu saldo é = R$ XX".'''

valorSaldo = 0

def depositar():
    global valorSaldo
    valorDeposito = float(input("Digite quanto você quer depositar: "))
    if (valorDeposito > 0):
        valorSaldo += valorDeposito
    else: 
        print("Opção inválida, tente novamente")

def sacar():
    global valorSaldo
    valorSaque = float(input("Digite o valor do seu saque: "))
    if (valorSaque > 0 or valorSaque < valorSaldo):
        valorSaldo -= valorSaque
    else:
        print("Opção inválida, tente novamente")

def saldo():
    print(f"Seu saldo é: R${valorSaldo}")

def menu():
    print("\n Menu")
    print(" 1 - Depositar \n 2 - Sacar \n 3 - Saldo \n 4 - Sair \n")

menu()
while(True):
    opcao = int(input("Digite uma opção: "))

    if (opcao == 1):
        depositar()
    elif (opcao == 2):
        sacar()
    elif(opcao == 3):
        saldo()
    elif(opcao == 4):
        print("Saindo...")
        break
    menu()