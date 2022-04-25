nomesAlunos = []
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
    opcao = int(input('Opção: '))

#Rodar este programa na IDLE do Phyton
