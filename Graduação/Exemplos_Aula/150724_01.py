'''Exceções'''

''' Tipos de Exceções
1. SyntaxError: Neste caso, se não estiver escrito corretamente, mostrará SyntaxError
    ex: print(

2. ZeroDivisionError: Neste caso, se for dividido por 0, mostrará ZeroDivisionError
    ex: divisor = int(input("Digite um número: "))
    print(10/divisor)

3. IndexError: Neste caso, se o indice não estiver presente na lista, mostrará IndexError
    ex: lista = [1, 10, 30]
    print(lista[4])
'''

'''Tratando erros
try:
    divisor = int(input("Digite um número: "))
except ValueError as e:
    print("Digite um número inteiro.")
    print(e)

try:
    print(10/divisor)
except ZeroDivisionError as e:
    print(f"A divisão não pode ser concluída, pois você tentou dividir por 0")
except Exception as e:
    print(f"A operação não pode ser realizada. Ocorreu um erro inesperado")'''

def menu():
    print("")

    print("** Menu **")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    print("")

    opcao = 0
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError as e:
        print("Digite um número de 1 a 5")
        print("")
    return opcao

#Calculadora
def somar():
    while(True):
        try:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite um outro número: "))

            if (num1 < 0 or num2 < 0):
                raise ValueError("Digite números maiores do que zero")
            print(f"A soma do número {num1} + {num2} é = {num1+num2}")
            print("")
            break
        except ValueError as e:
            print("Digite apenas números inteiros")

def subtrair():
    while(True):
        try:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite um outro número: "))
        except ValueError as e:
            print("Digite apenas números inteiros")
        else:
            print(f"A subtração do número {num1} - {num2} é = {num1-num2}")
            print("")
            break

def multiplicar():
    while(True):
        try:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite um outro número: "))
        except ValueError as e:
            print("Digite apenas números inteiros")
        else:
            print(f"A multiplicação do número {num1} * {num2} é = {num1*num2}")
            print("")
            break

def dividir():
    while(True):
        try:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite um outro número: "))
        except ValueError as e:
            print("Digite apenas números inteiros")
        try:
            print(f"A divisão do número {num1} / {num2} é = {num1/num2}")
            print("")
        except ZeroDivisionError as e:
            print("Você tentou dividir por 0!")
        else:
            break

while (True):
    opcao = menu()

    if (opcao == 1):
        print("** Soma **")
        somar()
    elif (opcao == 2):
        print("** Subtração **")
        subtrair()
    elif (opcao == 3):
        print("** Multiplicação **")
        multiplicar()
    elif (opcao == 4):
        print("** Divisão **")
        dividir()
    elif (opcao == 5):
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        print("")