'''Lista de Exercícios 00 (Revisão)
Instruções:
Desenvolva seu algoritmo para os problemas abaixo.
Crie suas próprias funções, não utilize funções preexistentes da linguagem.'''

'''Estrutura Sequencial
#1. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Digite 4 notas bimestrais \n")
media = 0

for i in range(4):
    nota = float(input(f"Nota {i+1}: "))
    media += nota

print(f"A média é: {media/4}")

#2. Faça um Programa que converta metros para centímetros.

metros = float(input("Digite o valor em metros para ser convertido: "))
cent = metros*100

print(f"O valor em centímetros é: {cent}")

#3. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Digite o quanto você ganha por hora: "))
numHoras = int(input("Digite o número de horas que você trabalha por mês: "))

totalSalario = salarioHora*numHoras

print(f"O total do salário np mês é de: {totalSalario}")

#4. Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

temp = float(input("Digite a temperatura em Farenheit: "))
tempCel = (5*(temp-32))/9

print(f"A temperatura em graus Celsius é de: {tempCel}")

#5. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo: [F/M] ")
pesoIdeal = 0

if (sexo.upper() == "F"):
    pesoIdeal = (62.1*altura) - 44.7
    print(f"O seu peso ideal é: {pesoIdeal}")
elif (sexo.upper() == "M"):
    pesoIdeal = (72.7*altura) - 58
    print(f"O seu peso ideal é: {pesoIdeal}")
else:
    print("Erro")'''

'''Estrutura de Decisão

#1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:
A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez.

print("Digite 4 notas bimestrais:")
somaNotas = 0

for i in range(4):
    nota = float(input(f"Nota {i+1}: "))
    somaNotas += nota

media = somaNotas/4
print(f"A média é: {media}")

if (media < 7):
    print("Reprovado")
elif(media >= 7):
    print("Aprovado")
elif(media == 10):
    print("Aprovado com Distinção")

#2. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = 0
menor = 999

if (num1 > num2 and num1 > num3):
    maior = num1
    if (num2 < num3):
        menor = num2
    else:
        menor = num3
elif (num2 > num1 and num2 > num3):
    maior = num2
    if (num1 < num3):
        menor = num1
    else: 
        menor = num3
else:
    maior = num3
    if (num1 < num2):
        menor = num1
    else:
        menor = num2

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#3. Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um número: "))

if (numero == 1):
    print("Domingo")
elif (numero == 2):
    print("Segunda")
elif (numero == 3):
    print("Terça")
elif (numero == 4):
    print("Quarta")
elif (numero == 5):
    print("Quinta")
elif (numero == 6):
    print("Sexta")
elif (numero == 7):
    print("Sábado")
else:
    print("Valor inválido")

#4. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados
for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

print("Digite três lados para um triângulo qualquer: ")
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado c: "))

if ((a+b)>c and (a+c)>b and (b+c)>a):
    print("Estas medidas formam um triângulo")
    print("Este triângulo é: ")
    if (a == b and a == c and b == c):
        print("Equilátero")
    elif (a == b or a == c or b == c):
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Estes lados não formam um triângulo")

#5. Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.

ano = int(input("Digite um ano: "))
if (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
    print("É bissexto")
else:
    print("Não é bissexto")'''

'''6. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
mesma é uma data válida.

#7. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número: "))

if (numero % 2 == 0):
    print("Este número é par")
else:
    print("Este número é ímpar")'''

'''Estrutura de Repetição

#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.

while(True):
    nota = float(input("Informe uma nota entre 0 e 10: "))
    if (nota > 0 and nota <=10):
        break
    else:
        continue

#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.

while(True):
    nomeUsuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if (senha == nomeUsuario):
        print("A senha não pode ser igual ao nome de usuário!")
        print("")
        continue
    else:
        print("Bem-Vind@")
        break

#3. Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

cresciA = 0.03
populacaoA = 80.000
cresciB = 0.015
populacaoB = 200.000
c = 0

while(populacaoA <= populacaoB):
    populacaoA += populacaoA*cresciA
    populacaoB += populacaoB*cresciB
    c+=1
print(f"Serão nescessários {c} anos para que a população da cidade A se iguale a população da cidade B")

#4. Faça um programa que leia 5 números e informe o maior número.

numeros = []
print("Digite 5 números: ")

for i in range(1, 6):
    num = float(input(f"Número {i}: "))
    numeros.append(num)

print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")

#5. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma, media = 0,0
print("Digite 5 números: ")

for i in range(1, 6):
    num = float(input(f"Número {i}: "))
    soma += num

media = soma/5
print(f"A soma dos números é: {soma} e a média é: {media}")

#6. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 5.

for i in range(1, 6):
    if (i % 2 != 0):
        print(i)'''

'''Mais questões disponíveis em https://wiki.python.org.br/ListaDeExercicios
(https://wiki.python.org.br/ListaDeExercicios)
The Huxley: www.thehuxley.com/ (http://www.thehuxley.com/)'''