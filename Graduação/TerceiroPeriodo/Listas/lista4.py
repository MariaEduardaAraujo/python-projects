'''Lista de Exercícios 03 (Recursividade)'''

'''#1. Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1

def fatorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fatorial(n-1)

fat = int(input("Digite o número para saber o seu fatorial: "))
print(fatorial(fat))

#2. Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

def inverte (p):
    if (len(p) == 0):
        return " "
    else:
        return p[-1] + inverte(p[:-1])

palavra = input("Digite uma palavra: ")
print(inverte(palavra))

3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
ocorre 2 vezes em "estrutura"

def conta (p, l):
    if (p == ""):
        return 0
    else:
        if (l == p[0]):
            return 1 + conta(p[1:], l)
        return conta(p[1:], l)

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")
print(conta(palavra, letra))

#4. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
ordem crescente.

def numero(n):
    if (n >= 0):
        r = numero(n-1)
        print(n, end=" ")

num = int(input("Digite o número natural qualquer: "))
numero(num)

#5. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
ordem decrescente.

def numero(n):
    if (n == 0):
        return 0
    else:
        print(n, end=" ")
        return numero(n-1)

num = int(input("Digite o número natural qualquer: "))
print(numero(num))

#6. Escreva uma função recursiva que calcule o N-ésimo 10 termo da sequencia de Fibonacci. A sequência de Fibonacci é
0,1, 1, 2, 3, 5, 8, 13, 21,...

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = int(input("Digite um número para saber o seu valor correspondente na Sequência de Fibonacci: "))
result = fibonacci(fib-1)
print(f"O {fib}° termo da Sequência de Fibonacci é {result}")

#7. Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número. O
fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15

def fatDuplo(n):
    if (n % 2 == 0):
        return "Número par"
    if (n == 1):
        return n
    else:
        return n * fatDuplo(n-2)

num = int(input("Digite um número ímpar: "))
print(f"Fatorial Duplo: {fatDuplo(num)}")

#8. Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da
mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

def palindromo(p):
    if (len(p) <= 1):
        return True
    elif (p[0] != p[-1]):
        return False
    return palindromo(p[1:-1])
    
palavra = input("Digite uma frase sem acentos e pontuações: ").split()
junta = "".join(palavra)
print(palindromo(junta))'''

'''9. O MDC de dois números inteiros é o maior número inteiro que divide ambos sem deixar resto. O MDC pode ser calculado
através do algoritmo de Euclides. Abaixo uma função iterativa que calcula o MDC. Reescreva a função abaixo de forma
recursiva.'''