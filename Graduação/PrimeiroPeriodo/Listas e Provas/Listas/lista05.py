import random

'''Q1. Elabore um algoritmo que efetue a soma de todos os números
ímpares que são múltiplos de três e que se encontram no conjunto
dos números de 1 até 500. No final, exiba a quantidade de números
ímpares múltiplos de 3, e o resultado da soma.

i = 1
soma = 0
multiplos = 0

while (i < 500):
    if (i % 2 != 0):
        if (i % 3 == 0):
            soma += i
            multiplos += 1
    i += 1
print(f"A quantidades de ímpares múltiplos de 3 de 1 a 500 é de: {multiplos}")
print(f"A soma desses números é de: {soma}")'''

'''Q2. Escreva um algoritmo que leia o nome e a altura de 10 pessoas,
e imprima o nome da maior e da menor pessoa.
maiorPessoa = 0;
menorPessoa = 0;
maiorAltura = 0;
menorAltura = 999;
i = 0

while (i < 3):
    altura = float(input("Digite a altura: "))
    nome = input("Digite um nome: ")

    if (altura > maiorAltura):
        maiorAltura = altura
        maiorPessoa = nome
    if (altura < menorAltura):
        menorAltura = altura
        menorPessoa = nome
    i += 1
print(f"O nome da maior pessoa é: {maiorPessoa}")
print(f"O nome da menor pessoa é {menorPessoa}")'''

'''Q3. Escreva um algoritmo que possui um número secreto de 1 a 100,
e fica pedindo que o usuário digite um número inteiro de 1 a 100 até
acertar o número secreto. Quando acertar, informar com quantos
chutes ele conseguiu acertar o número.

numSecreto = random.randint(1,100)
i = 0
tentativas = 0

while(i == 0):
    palpite = int(input("Digite um número de [1 a 100] "))
    if (palpite == numSecreto):
        print("Você acertou!")
        print(f"Você conseguiu acertar com {tentativas} tentativas")
        i+=1
    elif(palpite > numSecreto):
        print("O número secreto é menor")
    else:
        print("O número secreto é maior")
    tentativas+=1'''

'''Q4. Q4. Escreva um algoritmo que:
1) Solicita a área em que um estudante prestou o vestibular (humanas, saúde, exatas).
2) Define a pontuação de corte de cada área.
3) Solicita a quantidade de estudantes que a turma de um cursinho  pré-vestibular possui.
4)Para cada estudante:
a)Solicita a área que cada estudante prestou o vestibular.
b)Solicita a nota do ENEM.
c)Informe se o estudante foi classificado ou não. 
5)No final, o sistema deverá informar:
d)Quantos alunos foram classificados e quantos foram desclassificados para cada área. 
e)A porcentagem de alunos classificados e desclassificado no total.

notaCorteExatas = 800;
notaCorteHumanas = 750;
notaCorteBiologicas = 900;

qtdAlunosCursinho = int(input("Qual a quantidade de alunos do cursinho? "))

alunoAprovadoExatas = 0
alunoAprovadoHumanas = 0
alunoAprovadoBiologicas = 0

alunoReprovadoBiologicas = 0
alunoReprovadoExatas = 0
alunoReprovadoHumanas = 0

alunoExatas = 0
alunoHumanas = 0
alunoBiologicas = 0

for i in range(qtdAlunosCursinho):
    areaVestibular = int(input("Em qual área esse aluno prestou vestibular? [1 - Exatas, 2 - Humanas, 3 - Biológica]: "))
    mediaEnem = int(input("Média desse estudante no ENEM: "))
    if (areaVestibular == 1):
        if (mediaEnem >= notaCorteExatas):
            alunoAprovadoExatas += 1
            alunoExatas += 1
        elif (mediaEnem < notaCorteExatas):
            alunoReprovadoExatas += 1
            alunoExatas += 1
    elif (areaVestibular == 2):
        if (mediaEnem >= notaCorteHumanas):
            alunoAprovadoHumanas += 1
            alunoHumanas += 1
        elif (mediaEnem < notaCorteHumanas):
            alunoReprovadoHumanas += 1
            alunoHumanas += 1
    elif (areaVestibular == 3):
        if (mediaEnem >= notaCorteBiologicas):
            alunoAprovadoBiologicas += 1
            alunoBiologicas += 1
        elif (mediaEnem < notaCorteBiologicas):
            alunoReprovadoBiologicas += 1
            alunoBiologicas += 1
    else:
        print("Nota menor que a nota de corte")

aprovacaoExatasPorcentagem = (alunoAprovadoExatas/alunoExatas) * 100
reprovacaoExatasPorcentagem = (alunoReprovadoExatas/alunoExatas) * 100
aprovacaoHumanasPorcentagem = (alunoAprovadoHumanas/alunoHumanas) * 100
reprovacaoHumanasPorcentagem = (alunoReprovadoHumanas/alunoHumanas) * 100
aprovacaoBiologicasPorcentagem = (alunoAprovadoBiologicas/alunoBiologicas) * 100
reprovacaoBiologicasPorcentagem = (alunoReprovadoBiologicas/alunoBiologicas) * 100

alunoClassificadoTotal = ((alunoAprovadoExatas + alunoAprovadoHumanas + alunoAprovadoBiologicas)/qtdAlunosCursinho) * 100
alunoDesclassificadoTotal = ((alunoReprovadoExatas + alunoReprovadoHumanas + alunoReprovadoBiologicas)/qtdAlunosCursinho) * 100

print(f"Porcentagem de alunos aprovados e reprovados em Exatas: Aprovados: {aprovacaoExatasPorcentagem}, Reprovados: {reprovacaoExatasPorcentagem}")
print(f"Porcentagem de alunos aprovados e reprovados em Humanas: Aprovados: {aprovacaoHumanasPorcentagem}, Reprovados: {reprovacaoHumanasPorcentagem}")
print(f"Porcentagem de alunos aprovados e reprovados em Biológicas: Aprovados: {aprovacaoBiologicasPorcentagem}, Reprovados: {reprovacaoBiologicasPorcentagem}") 
print(f"Classificados e Desclassificados total: {alunoClassificadoTotal}, {alunoDesclassificadoTotal}")'''

'''Q5. Escreva um algoritmo que leia um valor inicial A e imprima a
sequência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 
Utilize o loop while para resolver esta questão.

numero = int(input("Digite um número: "))
fat = 1

print(f"{numero}! =", end=" ")

while(numero >= 1):
    if (numero == 1):
        print(f"{numero} =", end=" ")
    else:
        print(f"{numero} x", end=" ")
    fat *= numero
    numero -=1
print(fat)'''