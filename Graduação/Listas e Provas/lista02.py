'''Questão 3 da Lista02

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}. Você terá {idade + 10} anos daqui a 10 anos.")
'''

'''Questão 4 da Lista02

qtd_alunos = int(input("Digite a quantidade de alunos que você quer dar as notas: "))

for i in range(qtd_alunos):
  nota1 = float(input("Nota 1: "))
  nota2 = float(input("Nota 2: "))
  nota3 = float(input("Nota 3: "))
  nota4 = float(input("Nota 4: "))

  media =(nota1+nota2+nota3+nota4)/4
  print(f"A média é {media}")
'''

'''Questão 5 da Lista02
qtd = float(input("Digite a quantidade de metros que você deseja converter para centimetros: "))
conv = qtd*100

print(f"{qtd} metros equivale a {conv} centímetros")
'''

'''Questão 6 da Lista02

temp_celsius = float(input("Digite a temperatura em graus CELSIUS: "))

vF = temp_celsius * 1.8 + 32
vK = temp_celsius + 273.15

print(f"A temperatura em Fahrenheit é de {vF} graus")
print(f"A temperatura em Kelvin é de {vK} graus")
'''

'''Questão 7 da Lista02

largura = float(input("Digite o comprimento do retangulo: "))
comprimento = float(input("Digite a largura de um retangulo: "))

area = largura * comprimento
print(f"A area do retangulo é de {area}")
'''

'''Questão 8 da Lista02

pi = 3.1416
raio = float(input("Digite o raio do círculo: "))

area = pi * (raio**2)
print(f"A area do circulo é de {area}")
'''

'''Questão 9 da Lista02

base = float(input("Digite o valor da base do triangulo: "))
altura = float(input("Digite o valor da altura do triangulo: "))

area = (base * altura)/2
print(f"A area do triangulo é de {area}")
'''