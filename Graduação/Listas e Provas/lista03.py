''' Data: 27/12/2023 Autor: Maria Eduarda de Araújo Silva'''

'''Q1. Faça um algoritmo que lê dois números, e verifica se os dois números são iguais. 
Se forem iguais, escrever "São iguais", se não, escrever "Não são iguais".

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

if (numero1 == numero2):
    print("São iguais")
else:
    print("Não são iguais")'''

'''Q2. Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou igual ao segundo número. 
Se for, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}". 
Se não, escrever "O número {valor do número 1} é menor ou igual ao número {valor do número 2}".

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

if (numero1 >= numero2):
    print(f"O número {numero1} é maior ou igual ao número {numero2}")
else:
    print(f"O número {numero1} é menor ou igual ao número {numero2}")'''

'''Q3. Faça um algoritmo que lê dois números, e verifica se o primeiro número é menor ou igual ao segundo número. 
Se for, escrever "O número {valor do número 1} é menor ou igual ao número {valor do número 2}". 
Se não, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}".

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

if (numero1 <= numero2):
    print(f"O número {numero1} é menor ou igual ao número {numero2}")
else:
    print(f"O número {numero1} é maior ou igual ao número {numero2}")'''

'''Q4. Faça um algoritmo que lê dois números, e verifica se o primeiro número é igual ao segundo número. 
Se forem iguais, escrever "Números iguais". Se não, escrever "Números diferentes".

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))

if (numero1 == numero2):
    print("Números iguais.")
else:
    print("Números diferentes.")'''

'''Q5. Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, e a senha. 
Depois, pede que o usuário confirme novamente a senha. O sistema deverá verificar se as senhas digitadas são iguais.
Se forem iguais, informar que o cadastro está correto. Se não forem iguais, informar que o cadastro não 
foi realizado porque as senhas não conferem.

user = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
confSenha = input("Confirme sua senha: ")

if (senha == confSenha):
    print("Cadastro realizado com sucesso")
else:
    print("As senhas não são iguais")'''

'''Q6. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, 
mas que só permite compras à vista.

print("Bem-Vindo ao Sistema de Compras")

concluir = input("Deseja concluir a sua compra? (S/N) ")
concluir = concluir.upper()

if concluir == "S":
    vista = input("Você pagará sua compra à vista? (S/N) ")
    vista = vista.upper()

    if vista == "S":
        print("Condições aprovadas para concluir a compra")
    else:
        print("Você não atende a todos os critérios para que sua compra seja concluída.")
        print("Sua compra será cancelada") 
else:
    print("Sua compra será cancelada") '''
 
'''Q7. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, 
mas que só permite realizar a compra, se a pessoa tiver dinheiro para pagar à vista e se estiver com a anuidade 
de associação de produtor rural em dia.

compra = input("Deseja concluir a compra? (S/N) ")
compra = compra.upper()

if compra == "S":
    vista = input("Você pagará a vista? (S/N) ")
    vista = vista.upper()

    if vista == "S":
        anuid = input("A anuidade de associação de produtor rural está em dia? (S/N) ")
        anuid = anuid.upper()
        
        if anuid == "S":
            print("Condições aprovadas para concluir a compra")
        else:
            print("Você não atende a todos os critérios para que sua compra seja concluída.")
            print("Sua compra será cancelada")
    else: 
        print("Você não atende a todos os critérios para que sua compra seja concluída.")
        print("Sua compra será cancelada")
else:
    print("Sua compra será cancelada")'''

'''Q8. Elabore um algoritmo que solicita duas informações do usuário. A primeira, pergunta se possui bolsa 
família (S ou N), e a segunda, se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa 
família e possuir mais de três filhos, deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.

bolsafam = input("Você recebe Bolsa Família? (S/N) ")
bolsafam = bolsafam.upper()

filhos = input("Você tem 3 filhos ou mais? (S/N) ")
filhos = filhos.upper()

if bolsafam == "S" and filhos == "S":
    print("Tem direito à vaga de cotista")
else:
    print("Não tem direito")'''

'''Q9. Elabore um algoritmo para que só possa autorizar a entrada na loja, àqueles que estão com a anuidade de 
associação em dia ou pagar o valor de 25 reais na entrada.

entrar = input("Deseja entrar na loja? (S/N) ")
entrar = entrar.upper()

if entrar == "S":
    anuid = input("Você está com a anuidade da associação em dia? (S/N) ")
    anuid = anuid.upper()
    
    if anuid == "S":
        print("Bem-Vindo a loja da associação")
    else:
        pagar = input("Deseja pagar o valor de 25 reais para a entrada na loja? (S/N) ")
        pagar = pagar.upper()
        
        if pagar == "S":
            print("Bem-Vindo a loja da associação")
        else:
            print("Entendido. Até a próxima")
else:
    print("Entendido. Até a próxima")'''