'''Q1. Faça um programa que leia três valores para os lados de um triângulo, considerando 
lados como A, B e C. Verificar se os lados fornecidos formam um triângulo, e se for 
esta condição verdadeira, deve ser indicado o tipo de triângulo formado: isósceles, escaleno ou equilátero.

lado1 = float(input("Digite o lado A do triângulo: "))
lado2 = float(input("Digite o lado B do triângulo: "))
lado3 = float(input("Digite o lado C do triângulo: "))

if (lado1 == lado2 == lado3):
    print("Triângulo Equilátero")
elif (lado1 != lado2 != lado3):
    print("Triângulo Escaleno")
elif (lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2): #Na última verificação exibe "Escaleno"
    print("Triângulo Isósceles")'''

'''Q2. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

“Telefonou para a vítima? “ 
“Esteve no local do crime?” 
“Mora perto da vítima? “
“Devia para a vítima? “ 
“Já trabalhou com a vítima? “

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, 
entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.

print("Responda as seguintes perguntas apenas com S para SIM ou N para NÃO")

perg1 = input("Telefonou para a vítima? ").upper()
perg2 = input("Esteve no local do crime? ").upper()
perg3 = input("Mora perto da vítima? ").upper()
perg4 = input("Devia para a vítima? ").upper()
perg5 = input("Já trabalhou com a vítima? ").upper()

respostas_positivas = 0

if perg1 == "S":
    respostas_positivas += 1
if perg2 == "S":
    respostas_positivas += 1
if perg3 == "S":
    respostas_positivas += 1
if perg4 == "S":
    respostas_positivas += 1
if perg5 == "S":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é suspeito(a)!")
elif 3 <= respostas_positivas <= 4:
    print("Você é cúmplice!")
elif respostas_positivas == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente!")
'''

'''Q3. Faça um programa que receba três inteiros e diga qual deles é o maior e qual o menor.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
elif numero2 < menor:
    menor = numero2

if numero3 > maior:
    maior = numero3
elif numero3 < menor:
    menor = numero3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")'''