#Funções e Condições:
'''Q1. Escreva uma função que receba um número como parâmetro e retorne "Par" se o número 
for par e "Ímpar" se o número for ímpar.

def parImpar(numero):
    if(numero % 2 == 0):
        print("Par")
    else:
        print("Ímpar")

numero = int(input("Digite um número: "))
parImpar(numero)'''

'''Q2. Escreva uma função que receba um ano como parâmetro e retorne True se o ano for 
bissexto e False caso contrário.

def anoBiss(ano):
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(True)
    else:
        print(False)    
ano = int(input("Digite um ano: "))
anoBiss(ano)'''

#Listas e Laços de Repetição:
'''Q1. Escreva uma função que receba uma lista de números e retorne a média desses números.

def mediaNumerica(numeros):
    media = 0
    for n in numeros:
        media += n
    print(f"A média é: {media/len(numeros)}") #Ou sum(numeros) / len(numeros)

numeros = [1, 2, 3, 5, 8, 54, 12]
mediaNumerica(numeros)'''

'''Q2. Crie um programa que leia 5 números do usuário, armazene-os em uma lista e, em 
seguida, imprima a lista na ordem inversa.

numeros = []

for i in range(0, 5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print(f"A lista é ordem inversa é: {numeros[::-1]}")'''

#Try e Except:
'''Q1. Escreva um programa que peça ao usuário para digitar um número e tente convertê-lo 
para inteiro. Se o usuário não digitar um número válido, exiba uma mensagem de erro e peça 
novamente até que um número válido seja digitado.

while(True):
    try:
        numero = float(input("Digite um número: "))
        print(f"O número convertido para inteiro é: {int(numero)}")
        break
    except ValueError:
        print("Digite um número válido")
        continue'''

'''Q2. Escreva uma função que divida dois números fornecidos pelo usuário. Use try e except 
para tratar a divisão por zero e qualquer entrada inválida.

try:
    dividendo = int(input("Digite um número: "))
    divisor = int(input("Digite outro número: "))
except ValueError:
    print("Digite um número válido!")
except ZeroDivisionError:
    print("Você não pode dividir por zero!")
else:
    print(f"O resultado da divisão é: {dividendo/divisor}")'''

#Gerenciador de Tarefas:
'''Q1. Crie um programa que permita ao usuário gerenciar uma lista de tarefas. 
O programa deve permitir adicionar, remover e visualizar tarefas. Use funções para cada 
operação e manipule exceções para entradas inválidas.

tarefas = []

def menu():
    print(''Gerenciador de tarefas
      1. Adicionar uma tarefa
      2. Ver todas as tarefas
      3. Remover uma tarefa
      4. Sair'')
    
def adicionar():
    print()
    tarefa = input("Digite o título da sua tarefa: ")
    if (tarefa in tarefas):
        print("Você adicionou uma tarefa com o mesmo título")
        print()
    else:
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        print()

def visualizar():
    print()
    print(f"Lista de tarefas: {tarefas}")
    print()

def remover():
    print()
    remocao = input("Digite o título da tarefa que você quer remover: ")
    for t in tarefas:
        if (t == remocao):
            tarefas.remove(remocao)
            print("Tarefa removida!")
            print(tarefas)
            print()

while(True):
    menu()
    print()
    opcao = int(input("Digite uma opção: "))

    if(opcao == 1):
        adicionar()
    elif(opcao == 2):
        visualizar()
    elif (opcao == 3):
        remover()
    elif (opcao == 4):
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")'''

'''Q2. Crie uma calculadora que suporte as operações básicas (adição, subtração, 
multiplicação e divisão). Use funções para cada operação e try e except para lidar com 
entradas inválidas e divisão por zero.

def soma():
    while(True):
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
        except ValueError:
            print("Digite apenas números!")
            break
        else:
            print()
            print(f"{num1} + {num2} = {num1 + num2}")
            break

def subtracao():
    while(True):
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        else:
            print()
            print(f"{num1} - {num2} = {num1 - num2}")
            break

def multiplicacao():
    while(True):
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        else:
            print()
            print(f"{num1} x {num2} = {num1 * num2}")
            break

def divisao():
    while(True):
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite mais um número: "))

            if (num2 == 0):
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Não é possivel dividir por zero!")
            continue
        except ValueError:
            print("Digite apenas números!")
        else:
            print()
            print(f"{num1} + {num2} = {num1 / num2}")
            break

def menu():
    print()
    print(''Calculadora
      1. Somar
      2. Subtração
      3. Multiplicação
      4. Divisão
      5. Sair'')

while(True):
    menu()

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite uma opção válida!")
        continue
    
    if (opcao == 1):
        soma()
    elif (opcao == 2):
        subtracao()
    elif (opcao == 3):
        multiplicacao()
    elif (opcao == 4):
        divisao()
    elif(opcao == 5):
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")'''