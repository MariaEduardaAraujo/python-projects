'''Lista de Exercícios 01 (Revisão - Funções)
Instruções:
Desenvolva seu algoritmo para os problemas abaixo.
Crie suas próprias funções, não utilize funções preexistentes da linguagem.'''

'''#1. Faça uma função fatorial(n) que, dado um número N, calcule e retorne o fatorial de N. O fatorial de um número natural n,
representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. Exemplos: 5! = 1 x 2 x 3 x 4 x 5 = 120
0! = 1 https://www.thehuxley.com/problem/936?locale=pt_BR - Fatorial

def fatorial(n):
    fat = 1
    while(n >= 1):
        fat *= n
        n -=1
    return fat

numero = int(input("Digite um número qualquer: "))
print(f"O seu fatorial é: ")
print(fatorial(numero))

#2. Faça uma função eh_par(numero) que recebe um número inteiro e retorna True (verdadeiro) se o número for par, False
(falso) caso contrário.

def eh_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    
numero = int(input("Digite um número: "))
print(eh_par(numero))

#3. Faça uma função par_ou_impar(numero) que recebe um número inteiro e retorna “par” ou “impar”.

def eh_par(num):
    if (num % 2 == 0):
        print("Par")
    else:
        print("Ímpar")
    
numero = int(input("Digite um número: "))
eh_par(numero)

#4. Escreva uma função compare(a, b) que recebe dois números a e b como parâmetro e retorna 1 se a > b, 0 se a == b, e -1
se a < b.

def compare(a,b):
    if (a == b):
        return 0
    elif (a < b):
        return -1
    else:
        return 1

a = float(input("Digite um número: "))
b = float(input("Digite um segundo número: "))

print(compare(a,b))

#5. Faça uma função maior_de_2(num1, num2) que, dados dois números, retorna o maior deles.
https://www.thehuxley.com/problem/1060?locale=pt_BR - Maior de 2

def maior_de_2(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2
    
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))

print(maior_de_2(numero1, numero2))

#6. Faça uma função maior_de_3(num1, num2, num3)que, dados três números, retorna o maior deles.

def maior_de_3(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num3 and num2 > num1):
        return num2
    else:
        return num3
    
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))
numero3 = float(input("Digite um terceiro número: "))

print(maior_de_3(numero1, numero2, numero3))

#7. Faça uma função dia_da_semana(dia) que recebe como parâmetro um número e retorna o dia correspondente da
semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve retornar valor inválido.
https://www.thehuxley.com/problem/1311?locale=pt_BR

def dia_da_semana(dia):
    if (dia == 1):
        print("Domingo")
    elif (dia == 2):
        print("Segunda")
    elif (dia == 3):
        print("Terça")
    elif (dia == 4):
        print("Quarta")
    elif (dia == 5):
        print("Quinta")
    elif (dia == 6):
        print("Sexta")
    elif (dia == 7):
        print("Sábado")
    else:
        print("valor inválido")

diaSemana = int(input("Digite um número: "))
dia_da_semana(diaSemana)

#8. Faça uma função hipotenusa(cateto1, cateto2) que retorna o comprimento da hipotenusa de um triângulo retângulo dados
os comprimentos dos dois lados como parâmetros. https://www.thehuxley.com/problem/702?locale=pt_BR

import math 

def hipotenusa(cateto1, cateto2):
    if (cateto1 > 0 and cateto2 > 0):
        hip = math.sqrt(cateto1**2 + cateto2 ** 2)
        result = round(hip, 2)
        return result

cat1 = float(input("Digite o comprimento do primeiro lado: "))
cat2 = float(input("Digite o comprimento do segundo lado: "))

print(hipotenusa(cat1, cat2))

#9. Faça uma função eh_bissexto(ano) que recebe um ano como parâmetro e retorna True se o ano for bissexto e False caso
contrário https://www.thehuxley.com/problem/568?locale=pt_BR

def eh_bissexto(ano):
    if (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
        return True
    else:
        return False
    
anoBis = int(input("Digite um ano: "))
print(eh_bissexto(anoBis))'''

'''10. Faça uma função eh_data_valida(dia, mes, ano) que recebe como parâmetro três valores, representando dia, mês e ano.
Essa função deve retornar True se os valores formarem uma data válida, e False caso contrário
https://www.thehuxley.com/problem/1113?locale=pt_BR'''

'''#11. Faça uma função soma_numeros(numero) que recebe como parâmetro um número N, calcula a soma de todos os números
de 1 até ele e retorna o valor da soma. Exemplo: soma_numeros(7) = 28 , pois 1+2+3+4+5+6+7=28.

def soma_numeros(numero):
    soma = 0
    while (numero >= 1):
        soma += numero
        numero -= 1
    return soma

num = int(input("Digite um número: "))
print(soma_numeros(num))

#12. Faça uma função eh_primo(numero) que recebe como parâmetro um número inteiro e retorna True se ele é um número
primo e False caso contrário. Um número é primo quando ele é divisível somente por um e por ele mesmo.

def eh_primo(numero):
    for i in range(2, numero // 2 + 1):
        if (numero % i == 0):
            return False
    return True
    
num = int(input("Digite um número: "))
print(eh_primo(num))'''

'''13. A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo
subsequente corresponde a soma dos dois anteriores. Faça uma função Fibonacci(termo) que dado um número N
representando o n-ésimo termo da sequencia de Fibonacci, retorna a soma desses termos. Exemplo: Fibonacci(7) = 20 ,
pois os 7 primeiros termos da sequencia de Fibonacci são “0,1, 1, 2, 3, 5, 8” e sua soma é 20.'''