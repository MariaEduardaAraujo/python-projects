print('''Opções
1 - Cadastrar Salário
2 - Cadastrar Número de Filhos
3 - Média de Salário
4 - Média de filhos
5 - Maior Salário
6 - Percentual
7 - Sair''')
opcao = int(input('Opção desejada: '))
valorsalario = []
numfilhos = []
salariomaior = []

def salario():
    cadastrosalario = float(input('Salário: '))
    valorsalario.append(cadastrosalario)
    if cadastrosalario>1000:
        salariomaior.append(cadastrosalario)
        
def filhos():
    cadastrofilhos = int(input('Número de filhos: '))
    numfilhos.append(cadastrofilhos)
    
def media_salario():
    mediasalario = sum(valorsalario)
    print('Média dos salários: ', mediasalario/len(valorsalario))

def media_filhos():
    mediafilhos = sum(numfilhos)
    print('Média dos filhos: ', mediafilhos/len(numfilhos))

def maiorsalario():
    maior = max(valorsalario)
    print('Maior salário: ', maior)

def percentual():
    salariomil = len(salariomaior)/len(valorsalario)
    print('Percentual de pessoas que recebem mais de 1000: ',salariomil*100 )

while opcao!=7:
    if opcao==1:
        salario()
    elif opcao==2:
        filhos()
    elif opcao==3:
        media_salario()
    elif opcao==4:
        media_filhos()
    elif opcao==5:
        maiorsalario()
    elif opcao==6:
        percentual()
    opcao = int(input('Opção desejada: '))

