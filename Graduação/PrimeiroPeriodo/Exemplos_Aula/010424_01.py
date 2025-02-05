'''def teste():
    print("Testado")
teste()'''

#Calculadora
def somar():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    print(f"A soma do número {num1} + {num2} é = {num1+num2}")

def subtrair():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    print(f"A subtração do número {num1} - {num2} é = {num1-num2}")

def multiplicar():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    print(f"A multiplicação do número {num1} * {num2} é = {num1*num2}")

def dividir():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    print(f"A divisão do número {num1} / {num2} é = {num1/num2}")

print("Operações matemáticas")
print(" 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n")

while (True):
    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        print("Você escolheu somar...")
        somar()
    elif (opcao == 2):
        print("Você escolheu subtrair...")
        subtrair()
    elif (opcao == 3):
        print("Você escolheu multiplicar...")
        multiplicar()
    elif (opcao == 4):
        print("Você escolheu dividir...")
        dividir()
    else:
        print("Saindo...")
        break