'''
num = int(input("Digite um número: "))

if num % 2 != 0:
    print(f"O número {num} é ímpar")
else:
    print(f"O número {num} é par")
'''

'''
sex = input("Digite o seu gênero: F/M ")

if sex == "F" or sex == "f":
    print("Feminino")
elif sex == "M" or sex == "m":
    print("Masculino")
else:
    print("Erro")
'''
'''
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")
'''

print("Digite as notas do aluno")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media =(nota1+nota2+nota3+nota4)/4

if media >= 6:
    print("O aluno foi aprovado")
    print(media)
else:
    print("O aluno foi reprovado")
    print(media)