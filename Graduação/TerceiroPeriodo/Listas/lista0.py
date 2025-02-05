'''Revisando Lógica de Programação - Exercícios
Escreva programas Python para responder os exercícios abaixo. Não copie e cole de um exercício já existente! Aproveite para
praticar.'''

'''#1. Imprima a soma dos números entre 150 e 300.
soma = 0
for i in range(150,301):
    soma += i
print(f"A soma dos valores entre 150 e 300 é: {soma}")

#2. Armazena em uma lista todos os múltiplos de 3,entre 1 e 100. Imprima cada elemento da lista, um por linha.
multiplos = []

for num in range(1,101):
    if (num % 3 == 0):
        multiplos.append(num)
for n in range(len(multiplos)):
    print(multiplos[n])

#3. Calcule o fatorial de um numero qualquer. O fatorial de um número n é n * (n-1) * (n-2) * ... * 1.
O fatorial de 0 é 1
O fatorial de 1 é(0!) * 1 = 1
O fatorial de 2 é(1!) * 2 = 2
O fatorial de 3 é(2!) * 3 = 6
O fatorial de 4 é(3!) * 4 = 24

numero = int(input("Digite um número para descobrir o seu fatorial: "))
fat = 1

while(numero >= 1):
    fat *= numero
    numero -=1
print(fat)'''

'''#4. Imprima a seguinte tabela usando fors encadeados:
1
2 4
3 6 9
4 8 12 16
n n*2 n*3 .... n*n'''

'''#5. Escreva uma função em que, dada uma variável x com algum valor inteiro, temos um novo x de acordo com a seguinte
regra:
Se x é par, x = x / 2;
Se x é impar, x = 3 * x + 1;
Imprime x;

def novoX(x):
    if (x % 2 == 0):
      x = x/2
    else:
       x = 3 * x + 1
    return x

num = int(input("Digite um valor inteiro qualquer: "))
print(novoX(num))

#6. Escreva um programa que utiliza a função da questão [5] para alterar o valor de uma variável x. O programa deve parar
quando x tiver o valor final de 1.
Por exemplo, para x = 13,a saída será:
40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

numero = int(input("Digite um valor inteiro qualquer: "))

def novoX(num):
    global x
    if (num % 2 == 0):
      num = num /2
    else:
        num = 3 * num + 1
    x = num
    return x

print(novoX(numero))
while (x > 1):
   if (x != 1):
      print(novoX(x))
   else:
      break'''