##Dona Maria
""" prod = float(input('Digite um valor inicial (maior que zero): '))
soma = 0

while prod>0:
  prod = float(input('Valor: '))
  soma = soma+prod
  print(soma)

valores = int(input('Digite um valor inicial maior que zero: '))
soma = 0

while valores>0:
  valores = float(input('Digite o valor: '))
  soma+= valores

print(soma-valores) """

##Números
"""v = []
a = int(input('Digite um número de 0 a 1000: '))

while a>0 and a<1000:
  v.append(a)
  a = int(input('Digite outro número de 0 a 1000: '))
  maior = max(v)
  menor = min(v)
  soma = max(v)+min(v)
print('Maior: ', maior, '\nMenor: ', menor, '\nSoma: ', soma)"""

##CDS
""" cds = []
quantidade = int(input('Quantidade de CDs: '))
for i in range(0, quantidade):
  valorcd = int(input('Valor do CD: '))
  cds.append(valorcd)
  
valortotal = sum(cds)
valormedio = valortotal/quantidade
print('Valor Médio: ', valormedio, 'Valor total: ', valortotal) """

##Notas.py
""" alunos = [] 
for i in range(5):
  nota1 = eval(input('Nota 1: '))
  nota2 = eval(input('Nota 2: '))
  nota3 = eval(input('Nota 3: '))
  nota4 = eval(input('Nota 4: '))

qtdfaltas = eval(input('Quantidade de faltas: '))
media =(nota1*2+nota2*3+nota3*1+nota4*4)/10
faltas = qtdfaltas*0.01

if media>6 and faltas<25:
  print('Aprovado com média', media)
  nome = input('Nome do aluno: ')
  alunos.append(nome)
elif media<3 or faltas>25:
    print('Reprovado')
print(alunos) """
