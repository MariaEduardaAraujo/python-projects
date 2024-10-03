'''with open("meu_nome.txt", "w", encoding="UTF-8") as arquivo:
    arquivo.write("OI")'''

#Exercícios
'''Agenda'''
'''Faça um programa como um formulário, que solicite do usuário: Nome, 
Idade, Sexo (M ou F) e Telefone.
Coloque o código dentro de uma função, e este código deve repetir até 
o usuário digitar '0' (para o Nome) informando que ele deseja encerrar
Dica: Salve estas informações em um arquivo, separando cada dado pela 
barra vertical (pipe) '|' No final da linha (após telefone) adiciona 
um '\n' '''
'''Média de Idades:
    1 - Média de idade;
    2 - Qual é a pessoa mais velha;
    3 - Telefone da pessoa mais jovem;'''

arquivo = open("dados.txt", "a", encoding="UTF-8")

def cadastro():
    while(True):
        nome = str(input("Digite um nome: "))
        if(nome != '0'):
            idade = input("Digite a idade: ")
            sexo = str(input("Digite o sexo: [F/M] ")).upper()
            telefone = str(input("Digite o telefone: [00] "))
            
            linha = f"{nome}|{idade}|{sexo}|{telefone}\n"
            arquivo.write(linha)
            arquivo.flush()
            
            print()
            print("Dados salvos com sucesso!\n")
        else:
            break

def media():
    arquivo = open("dados.txt", "r", encoding="UTF-8")

    print('''Cálculo de Média de Idades:
    1 - Média de idade;
    2 - Qual é a pessoa mais velha;
    3 - Telefone da pessoa mais jovem;''')

    mediaIdade = 0
    cont = 0

    op = int(input("Qual a opção que você deseja? "))

    if (op == 1):
        for media in arquivo:
            i = media.split("|")
            mediaIdade += int(i[1])
            cont+=1
        print(f"A média de idades é: {mediaIdade/cont} anos")
    elif (op == 2):
        idadeMaisVelho = 0
        nomeMaisVelho = ""
        for media in arquivo:
            i = media.split("|")
            maiorIdade = int(i[1])        
            if (maiorIdade > idadeMaisVelho):
                idadeMaisVelho = maiorIdade
                nomeMaisVelho = i[0]
        print(f"A pessoa mais velha é: {nomeMaisVelho.capitalize()}")
    elif (op == 3):
        idadeMaisNovo = 999
        telefoneMaisNovo = ""
        for media in arquivo:
            i = media.split("|")
            menorIdade = int(i[1])   
            if (menorIdade < idadeMaisNovo):
                idadeMaisNovo = menorIdade
                telefoneMaisNovo = i[3]
        print(f"O telefone da pessoa mais nova é: {telefoneMaisNovo}")

cadastro()

op = str(input("Calcular média? [S/N] ")).upper()
if (op == "S"):
    media()
else:
    exit()