#Ímpar ou Par
def verificaSeNumeroParOuImpar(numero):
    if(numero % 2 == 0):
        print("Par");
    else:
        print("Impar");

while (True):
    numero = int(input("Digite um número qualquer: "));
    if(numero >= 0):
        verificaSeNumeroParOuImpar(numero);
    else:
        break;

#Verificação Idade
capacidade = 3;
qtd_acessaram = 0;

def validarEntrada(nome, idade):
    global qtd_acessaram;
    
    if(idade >= 18):
        print(f"Pode entrar {nome}");
        qtd_acessaram = qtd_acessaram + 1;
    else:
        print(f"Não pode entrar {nome}");

while(qtd_acessaram < capacidade):
    print("Bem vindos à festa");
    nome = input("Qual o seu nome? ");
    idade = int(input("Qual a sua idade? "));
    
    validarEntrada(nome, idade);

#Verificação Idade com Retorno
limite_boate = 5

def validar_entrada(idade):
    if (idade >= 18):
        return True
    else:
        return False
    
while(limite_boate > 1):
    idade = int(input("Digite a sua idade: "))

    '''retorno = validar_entrada(idade)
       if(retorno == True)
       if(validar_entrada(idade) == True)'''
    
    if (validar_entrada(idade)):
        print("Acesso liberado")
        limite_boate -= 1
    else:
        print("Acesso negado")