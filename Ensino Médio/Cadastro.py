print('Academia')
print('1 - Cadastrar clientes')
print('2 - Cadastrar funcionários')
print('3 - Cadastrar exercícios')
print('4 - Saber quantos exercícios cada cliente fez')
print('5 - Exibir exercícos cadastrados')
print('6 - Saber quais foram todos os exercícios feito pelos clientes')
print('7 - Sair')

clientes = []
funcionarios = []
exercicios = []
exercicioCliente = []

opcao = int(input('Opção desejada: '))

def cadastro():
    cliente = {}
    nome = input('Nome: ')
    email = input('E-mail: ')
    idade = int(input('Idade: '))
    
    cliente['Nome'] = nome
    cliente['E-mail'] = email
    cliente['Idade']= idade
    clientes.append(cliente)

def cadastroF():
    funcionario = {}
    nome = input('Nome: ')
    empresa = input('Empresa: ')

    funcionario['Nome'] = nome
    funcionario['Empresa'] = empresa
    funcionarios.append(funcionario)
    
def cadastroExerc():
    numExercicios = int(input('Quantos exercícios você quer cadastrar: '))
    for i in range(numExercicios):
        exercicio = input('Exercício para ser cadastrado: ')
        exercicios.append(exercicio)
        print('Exercício cadastrado!')

def QntExercCliente():
    perg1 = input('Exercício: ')
    quantidade = 0
    for cliente in clientes:
        if perg1 in exercicios:
            quantidade = quantidade + 1
            exercicioCliente.append(perg1)
        print('Exercícios do cliente: ', quantidade)


def exerciciosCadastrados():
    print('Exercícios cadastrados: ', exercicios)

def exerciciosCliente():
    print('Exercício do cliente: ', exercicioCliente)

while opcao!=7:
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        cadastroF()
    elif opcao == 3:
        cadastroExerc()
    elif opcao == 4:
        QntExercCliente()
    elif opcao == 5:
        exerciciosCadastrados()
    elif opcao == 6:
        exerciciosCliente()
    opcao = int(input('Opção desejada: '))
