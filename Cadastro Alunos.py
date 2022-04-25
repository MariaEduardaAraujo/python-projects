## Cadastro Alunos 2
""" nomesAlunos = []
print('''   Menu
            1- Cadastrar
            2 - Gravar
            3 - Sair''')

opcao = int(input('Opção: '))

def cadastro():
    nome = input('Nome: ')
    nomesAlunos.append(nome)
def gravar():
    arq = open('Nome.txt', 'r+')
    nomesAlunos.writeline('Lista\n')
    arq.writelines(nomesAlunos)
    arq.close()

while opcao!=3:
    if opcao==1:
        cadastro()
    elif opcao==2:
        gravar()
    opcao = int(input('Opção: ')) """

#Rodar este programa na IDLE do Phyton

## Cadastro Alunos 2
""" nomesAlunos = []
print('''   Menu
            1- Cadastrar
            2 - Gravar
            3 - Sair''')

opcao = int(input('Opção: '))

def cadastro():
    nome = input('Nome: ')
    
def gravar():
    arq = open('nome.txt', 'r+')
    nomesAlunos.append('Lista Nomes\n')
    nomesAlunos.append('--------------\n')
    arq.writeline(nomesAlunos)
    arq.close()

while opcao!=3:
    if opcao==1:
        cadastro()
    elif opcao==2:
        gravar()
    opcao = int(input('Opção: ')) """
