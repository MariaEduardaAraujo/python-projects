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

#Capacidade
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
    nome = input("Qualo seu nome? ");
    idade = int(input("Qual a sua idade? "));
    
    validarEntrada(nome, idade);