nomeConvidados = ["A", "B", "C"]
numero_externo = 0

def validar_cpf(numCpf):
    print(f"O CPF é: {numCpf}")

def validar_nome(nome):
    print(f"Seu nome é: {nome}")

def validar_convidados(nome, idade):
    global nomeConvidados

    if (nome in nomeConvidados):
        if (idade >= 18):
            print("Acesso liberado")
    else: 
        print("Acesso negado")

def numero_com_parametro(numero):
    global numero_externo
    numero_externo = 1000

    print(f"Imprimindo na função o número: {numero_externo}")

numero_externo = 10
print(numero_externo)
numero_com_parametro(1)

#Sobreposição não funciona
'''
def validar_numero():
    num = int(input("Digite um número: "))

    if (num <= 0):
        print("Número inválido")
    else:
        print("Número válido")

def validar_numero(numero):
    if (numero <= 0):
        print("Número inválido")
    else:
        print("Número válido")'''