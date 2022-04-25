opcao = int(input('Op: '))
nomesAlunos = []

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
    opcao = int(input('Op: '))
