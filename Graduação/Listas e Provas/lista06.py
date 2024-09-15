'''Q1. (FOR) Elabore um algoritmo que simule uma tabuada.

for i in range (1,11):
    print(f"Tabuada do {i}")
    for x in range (0,11):
        print(f"{i}x{x} =", i*x)
    print(" ")'''

'''Q2. (FOR e LISTAS) Elabore um algoritmo que pergunta a quantidade de alunos que a turma possui. 
Depois individualmente solicita as suas 4 médias bimestrais. Após, calcule a média de cada aluno. Ao final:
Informe quantos alunos foram aprovados, e quantos foram reprovados, sabendo que para ser aprovado, 
o aluno deve atingir no mínimio 6 na média final. Informe a maior, e a menor média final.

qtdAlunos = int(input("Quantos alunos turma possui? "))

alunosAprovados = []
alunosReprovados = []
medias = []

for i in range(qtdAlunos):
    nota1 = float(input(f"Digite a primeira nota do aluno {i}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {i}: "))
    nota3 = float(input(f"Digite a terceira nota do aluno {i}: "))
    nota4 = float(input(f"Digite a quarta nota do aluno {i}: "))

    media = (nota1 + nota2 + nota3 + nota4)/4
    medias.append(media)
    
    if (media >= 6):
        alunosAprovados.insert(i, media)
    else:
        alunosReprovados.insert(i, media)

mediaFinalMaior = max(medias)
mediaFinalMenor = min(medias)

print(f"A quantidade de alunos aprovados é de: {len(alunosAprovados)}") 
print(f"A quantidade de alunos reprovados é de: {len(alunosReprovados)}") 
print(f"A maior média é: {mediaFinalMaior} e a menor média é: {mediaFinalMenor}")'''

'''Outra solução da Q2
qtdAlunos = int(input("Quantos alunos turma possui? "))
alunosAprovados = 0
alunosReprovados = 0
mediaFinalMaior = 0
mediaFinalMenor = 0

for i in range(qtdAlunos):
    somaNotas = 0
    for n in range(1, 5):
        while True:
            notas = float(input(f"Digite a {n} nota do aluno {i+1}: "))
            if (notas <= 10 and notas >= 0):
                somaNotas += notas
                break
            else:
                print("Nota inválida")

    media = (somaNotas)/4

    if (media >= 6):
        alunosAprovados += 1
        if (mediaFinalMaior <= media):
            mediaFinalMaior = media
    else:
        alunosReprovados += 1
        if (mediaFinalMenor <= media):
            mediaFinalMenor = media

print(f"A quantidade de alunos aprovados é de: {alunosAprovados}") 
print(f"A quantidade de alunos reprovados é de: {alunosReprovados}") 
print(f"A maior média é: {mediaFinalMaior} e a menor média é: {mediaFinalMenor}")'''

'''Q3. (WHILE, FOR e LISTAS) Elabore um algoritmo que entra em loop solicitando um número inteiro, e só para de 
pedir um novo número quando for digitado um número negativo. Para cada número inteiro positivo digitado, deve 
verificar se este número é ou não um número primo (um número primo é aquele que é divisível somente por ele mesmo 
e por 1. O número um por sí só já é primo). 
Ao final, o programa deve informar:
1) A quantidade de números primos digitados.
2) A quantidade de números digitados que não são primos.

primos = 0
naoPrimos = 0

while True:
    numero = int(input("Digite um número inteiro: [Diferente de 0]"))
    if (numero > 0):
        if (numero != 1):
            primo = True
            for i in range(2, int(numero**0.5) + 1):
                if (numero % i == 0):
                    primo = False
                    break
            if primo:
                primos += 1
            else:
                naoPrimos += 1
    else:
        break

print(f"Foram digitados {primos} números primos")
print(f"Foram digitados {naoPrimos} números que não são primos")'''

#Não fiz
'''Q4. Em um prédio há 16 apartamentos (1 a 16) e três elevadores (A, B e C). 
Foi realizada uma pesquisa no qual cada apartamento respondia:
1) O número do apartamento;
2) O elevador que utiliza com mais frequência;
3) E o período que em mais utiliza este elevador:
'M' = matutino
'V' = vespertino
'N' = noturno

Construa um algoritmo que calcula e imprime:
1) Qual o elevador mais frequentado e em qual período se concentra o maior fluxo;
2) Qual o período mais usado de todos e a que elevador pertence;
3) Qual a diferença percentual entre o elevador mais usado dos períodos e o menos usado.'''

'''Q5. (WHILE, FOR e LISTAS) Elabore um algoritmo que simula um sistema de venda para uma lanchonete. O sistema deve iniciar um menu que possui 4 opções.
1) Opção 1  (Escolher produtos): lista os produtos que a lanchonete possui com os respectivos preços unitários (usar listas multidimensional, produto -> preço). Exemplo: produtos = [["Misto", 3.4], ["Refrigerante", 2.5]]
Em Opção 1, deve-se entrar em loop, e pedir para o usuário escolher uma opção e a quantidade desejada do produto. 
Cada produto escolhido, deve ser adicionado em uma lista de produtos escolhidos, armazenando o nome do produto, a quantidade, o valor unitário.
Deve também, possuir uma opção para sair dessa Opção 1 e retornar ao menu principal.
2) Opção 2 (Remover produtos): deve listar os produtos que foram adicionados para compra, e oferecer a opção de remover algum produto.
3) Opção 3 (Relatório de venda): deve apresentar um quadro geral de venda, mostrando cada produto comprado, a quantidade escolhida, e o 
valor total para cada produto comprado. Após, o valor total da compra.
4) Opção 4 (Sair): deve encerrar o programa. 

produtos = [["MISTO", 5], ["REFRIGERANTE", 3.5], ["ÁGUA", 1.5], ["PIPOCA", 1]]
produtosEscolhidos = []
tot_pag = 0

print(" ======= Menu =======")
print(" 1. Escolher Produtos \n 2. Remover produtos \n 3. Relatório de Vendas \n 4. Sair \n")

while (True):
    op = int(input("Escolha uma opção: "))

    if (op == 1):
        print(produtos, "\n")
        item = input("Escolha um lanche: ").upper()
        qtdLanche = int(input("Quantos lanches você deseja? "))
        
        if (item == "MISTO"):
            tot_pag = tot_pag+(5*qtdLanche)
            totMisto = 5*qtdLanche
            produtosEscolhidos.append([item, qtdLanche, totMisto])
        elif (item == "REFRIGERANTE"):
            tot_pag = tot_pag+(3.5*qtdLanche)
            totRefri = 3.5*qtdLanche
            produtosEscolhidos.append([item, qtdLanche, totRefri])
        elif (item == "ÁGUA"):
            tot_pag = tot_pag+(1.50*qtdLanche)
            totAgua = 1.50*qtdLanche
            produtosEscolhidos.append([item, qtdLanche, totAgua])
        elif (item == "PIPOCA"):
            tot_pag = tot_pag+(1*qtdLanche)
            totPipoca = 1*qtdLanche
            produtosEscolhidos.append([item, qtdLanche, totPipoca])
        else:
            print("Valor inválido")
            continue
        print("="*20)
        
    elif (op == 3):
        valorTotal = tot_pag
        print(f"Produtos vendidos: {produtosEscolhidos}")
        print(f"Valor total: R${valorTotal}")
        print("="*20)

    elif (op == 4):
        print("Saindo...")
        break

    else:
        print("Erro inesperado")
'''

#Não funciona corretamente
'''elif (op == 2):
    for produto in produtosEscolhidos:
        lanche = input("Digite o nome do produto que você quer remover: ")
        if produto == lanche:
            produtosEscolhidos.remove(produto)
            print("Item removido")
            break
    print("="*20)'''