#Prática
def lerNomes():
    arquivo = open("meu_nome.txt", "r", encoding="UTF-8")
    nomes = arquivo.read()
    lista = nomes.split(";")

    for n in lista:
        print(n)

    arquivo.close()

def escreveNomes(nomes):
    #arquivo = open("meu_nome.txt", "a", encoding="UTF-8")
    #arquivo.write("Jose; Lucio; Tereza")

    arquivo = open("meu_nome.txt", "a", encoding="UTF-8")
    arquivo.write(nomes)
    arquivo.close()

escreveNomes("Paulo; João; ")
lerNomes()

#Exercícios
'''Questão 1
''Faça um programa como um formulário, que solicite do usuário: Nome, 
Idade, Sexo (M ou F) e Telefone.
Coloque o código dentro de uma função, e este código deve repetir até 
o usuário digitar '0' (para o Nome) informando que ele deseja encerrar
Dica: Salve estas informações em um arquivo, separando cada dado pela 
barra vertical (pipe) '|' No final da linha (após telefone) adiciona 
um '\n' ''

arquivo = open("dados.txt", "a", encoding="UTF-8")

def cadastro():
    while(True):
        nome = str(input("Digite um nome: "))
        if(nome != '0'):
            idade = input("Digite a idade: ")
            sexo = str(input("Digite o sexo: [F/M] "))
            telefone = str(input("Digite o telefone: [00] "))
            
            linha = f"{nome} | {idade} | {sexo} | {telefone}\n"
            arquivo.write(linha)
            print()
            print("Dados salvos com sucesso!\n")

        else:
            print("Saindo...")
            break
cadastro()'''

'''Questão 2
'' Agora, no mesmo arquivo, crie uma função para ler estes dados,
imprimindo de forma organizada, algo como:
Nome: José da Silva
Idade: 20 anos #concatene 'anos' sempre depois da idade
Sexo: Masculino #Deve ter um IF para verificar se é M ou F
Telefone: 88888888''

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
            print()
            print("Dados salvos com sucesso!\n")

        else:
            break

def leitura():
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for nome in arquivo:
        d = nome.split("|")
        print()
        print(f"Nome: {d[0]}")
        print(f"Idade: {d[1]} anos")
        if(d[2] == "F"):
            print(f"Sexo: Feminino")
        elif(d[2] == "M"):
            print(f"Sexo: Masculino")
        print(f"Telefone: {d[3]}")

cadastro()
leitura()'''

'''Questão 3
''No mesmo arquivo, crie uma função que recebe como parâmetro o sexo 
e RETORNA uma lista com todos os cadastros do sexo especificado: ''

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
            print()
            print("Dados salvos com sucesso!\n")
        else:
            break

def leitura():
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for nome in arquivo:
        d = nome.split("|")
        print()
        print(f"Nome: {d[0]}")
        print(f"Idade: {d[1]} anos")
        if(d[2] == "F"):
            print(f"Sexo: Feminino")
        elif(d[2] == "M"):
            print(f"Sexo: Masculino")
        print(f"Telefone: {d[3]}")

def buscaPeloSexo(sexoProcurado):
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for dado in arquivo:
        s = dado.split("|")
        if(sexoProcurado == s[2]):
            if(s[2] == "F"):
                print(f"Usuários do sexo Feminino: {s}")
            elif(s[2] == "M"):
                print(f"Usuários do sexo Masculino: {s}")
        ''else:
            print("Sexo não localizado")''

cadastro()
leitura()

sexoProcurado = input("Digite o sexo que você quer retornar: [F/M] ").upper()
buscaPeloSexo(sexoProcurado)'''

'''Questão Extra
No mesmo arquivo, crie uma função que recebe como parâmetro um nome,
ou parte dele, e RETORNA uma lista com todos os cadastros que tenham o
nome igual ao valor passado como parâmetro ou possuam parte do nome com
o valor passado como parâmetro '''
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
            print()
            print("Dados salvos com sucesso!\n")
        else:
            break

def leitura():
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for nome in arquivo:
        d = nome.split("|")
        print()
        print(f"Nome: {d[0]}")
        print(f"Idade: {d[1]} anos")
        if(d[2] == "F"):
            print(f"Sexo: Feminino")
        elif(d[2] == "M"):
            print(f"Sexo: Masculino")
        print(f"Telefone: {d[3]}")

def buscaPeloSexo(sexoProcurado):
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for dado in arquivo:
        s = dado.split("|")
        if(sexoProcurado == s[2]):
            if(s[2] == "F"):
                print(f"Usuários do sexo Feminino: {s}")
            elif(s[2] == "M"):
                print(f"Usuários do sexo Masculino: {s}")
        '''else:
            print("Sexo não localizado")'''

def buscaPeloNome(nomeProcurado):
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for dado in arquivo:
        n = dado.split("|")
        p = "".join(n[0])
        if (nomeProcurado in p):
            print(f"Possíveis pessoas que você está procurando: {n}")
        '''else:
            print("Pessoa não localizada")'''
cadastro()
leitura()

sexoProcurado = input("Digite o sexo que você quer retornar: [F/M] ").upper()
buscaPeloSexo(sexoProcurado)
nomeProcurado = input("Digite o nome, ou parte dele, que você quer localizar: ")
buscaPeloNome(nomeProcurado)