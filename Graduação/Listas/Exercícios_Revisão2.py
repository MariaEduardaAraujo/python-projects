#Funções e Condições
'''Q1. Escreva uma função que receba um número inteiro e retorne True se o número for primo e 
False caso contrário.
def primos(numero):
    if (numero < 2):
        return False
    for i in range(2, int(numero**0.5) + 1):
            if (numero % i == 0):
                return False
    return True

numero = int(input("Digite um número: "))
print(primos(numero))''' 
 
'''Q2. Escreva uma função que receba um texto e retorne o texto invertido.

def inverTexto (texto):
     return texto[::-1]

texto = input("Digite um texto: ")
print(inverTexto(texto))'''

#Listas e Laços de Repetição:
'''Q1. Escreva uma função que receba uma lista de números e retorne a lista com os números 
ordenados em ordem crescente.

def ordenarNumeros (numeros):
    listaOrdenada = sorted(numeros)
    print(f"Lista ordenada: {listaOrdenada}")

numeros = [6, 7, 10, 12, 20, 15, 32, 45, 5, 55]
ordenarNumeros(numeros)'''

'''Q2. Crie um programa que leia uma lista de 10 números do usuário e, em seguida, encontre o 
maior e o menor número da lista.

numeros = []

for i in range(10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print(f"Maior número da lista: {max(numeros)}")
print(f"Menor número da lista: {min(numeros)}")'''

#Try e Except:
'''Q1. Escreva um programa que peça ao usuário para digitar uma lista de números separados 
por espaço e tente converter cada um para inteiro. Se houver algum valor inválido, exiba 
uma mensagem de erro e peça para o usuário digitar novamente.

numeros = []
while(True):
    try:
        numero = input("Digite uma lista de números, separados por espaço: ")
        if not numero.strip():  # Verifica se a entrada é vazia ou contém apenas espaços em branco
            raise ValueError
        for i in numero.split(" "):
            numeros.append(int(i))
    except ValueError:
        print("Digite uma entrada válida!")
    break

print(numeros)'''

'''Q2. Escreva uma função que receba uma lista de números e um índice, e retorne o elemento na 
posição do índice. Use try e except para tratar o caso de índices fora do intervalo da 
lista.

def retorna(numeros, indice):
    print(f"O número no índice {indice} é: {numeros[indice]}")

numeros = [6, 7, 10, 12, 20, 15, 32, 45, 5, 55]

try:
    indice = int(input("Digite o índice que você quer retornar: "))
    if(indice <= len(numeros)):
        retorna(numeros, indice)
    else:    
        raise IndexError
except IndexError:
    print("Este índice não está presente na lista")
except ValueError:
    print("Por favor, digite um número inteiro válido.")'''

#Sistema de Biblioteca:
'''Crie um programa que permita ao usuário gerenciar uma biblioteca. O programa deve 
permitir adicionar, remover e visualizar livros, cada um com título, autor e ano de 
publicação. Use funções para cada operação e manipule exceções para entradas inválidas.

biblioteca = []
def adicionar():
    try:
        titulo = input("Título do livro: ")
        ano = int(input("Ano de publicação: "))
        autor = input("Autor do livro: ")

        if (titulo.strip() == "" or autor.strip() == ""):
            raise ValueError ("O título ou o autor não podem ser vazios")
        else:
            biblioteca.append((titulo, ano, autor))
            print()
            print("Livro adicionado!")
            print()
    except ValueError:
        print()
        print("Digite um valor aceito!")
        print()

def visualizar():
    print()
    if(len(biblioteca) > 0):
        print(f"Livros cadastrados na biblioteca: ")
        for l in biblioteca:
            print(l)
        print()
    else:
        print("Não há livros cadastrados!")
        print()

def remover():
    try:
        if (len(biblioteca) > 0):
            remocao = input("Qual o título que você deseja remover? ")
            for l in biblioteca:
                if (remocao == l[0]):
                    biblioteca.remove(l)
                    print("Livro removido")
        else:
            print("Não há o que remover!")
    except Exception:
        print("Valor não encontrado!")

def menu():
    print(''Sistema de Biblioteca
      1. Adicionar livros
      2. Visualizar livros
      3. Remover livros
      4. Sair'')
    print()

while(True):
    print()
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        print()
    except ValueError:
        print("Digite apenas um número inteiro")
        print()
        continue

    if (opcao == 1):
        adicionar()
    elif (opcao == 2):
        visualizar()
    elif (opcao == 3):
        remover()
    elif (opcao == 4):
        print("Saindo...")
        break
    else:
        print("Opção inválida!")'''

#Jogo da Forca:
'''Crie um jogo da forca onde o usuário deve adivinhar uma palavra secreta. O programa deve
permitir que o usuário insira letras e verificar se a letra está na palavra. Use listas, 
laços de repetição, funções e manipule exceções para entradas inválidas.'''

#Conversor de Temperatura:
'''Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O 
programa deve permitir que o usuário escolha a unidade de entrada e a unidade de saída, e 
realizar a conversão. Use funções, laços de repetição, e try e except para tratar entradas 
inválidas.'''

def cf():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Fahrenheit: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorCF = (temp * 9) / 5 + 32;
        print(f"A temperatura convertida é: {conversorCF}")

def ck():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Kelvin: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorCK = temp + 273.15
        print(f"A temperatura convertida é: {conversorCK}")

def fc():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Celcius: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorFC = ((temp - 32) * 5) / 9;
        print(f"A temperatura convertida é: {conversorFC}")

def fk():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Kelvin: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorFK = ((temp - 32) * 5) / 9 + 273.15;
        print(f"A temperatura convertida é: {conversorFK}")

def kc():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Celcius: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorKC = temp - 273.15;
        print(f"A temperatura convertida é: {conversorKC}")

def kf():
    try:
        temp = float(input("Digite a temperatura que você quer converter para Fahrenheit: "))
    except ValueError:
        print("Insira apenas números!")
    else:
        conversorKF = ((temp - 273.15) * 9) / 5 + 32;
        print(f"A temperatura convertida é: {conversorKF}")

while(True):
    try:
        entrada = input("Digite a entrada que você deseja converter: [C/F/K] ").upper()
        saida = input("Digite a saída que você deseja converter: [C/F/K] ").upper()

        if (entrada.strip() == "" or saida.strip() == ""):
            raise ValueError("Entrada ou saída não podem ser vazios!")
    except ValueError:
        print("Digite uma entrada válida!")
        continue

    if (entrada.strip() == "C"):
        if (saida.strip() == "F"):
            cf()
        elif (saida.strip() == "K"):
            ck()
    elif (entrada.strip() == "F"):
        if (saida.strip() == "C"):
            fc()
        elif (saida.strip() == "K"):
            fk()
    elif (entrada.strip() == "K"):
        if (saida.strip() == "C"):
            kc()
        elif (saida.strip() == "F"):
            kf()
    else:
        print("Opção inválida!")
    
    continuar = input("Deseja continuar convertendo? [S/N] ").upper()
    if (continuar == "S"):
        continue
    else:
        break