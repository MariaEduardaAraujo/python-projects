# Maria Eduarda e Raphael

#Questao 1
'''qtd_pessoas = int(input("De quantas pessoas você quer calcular o IMC? "))
imcs = []
abaixo = 0
normal = 0
p_acima = 0
acima = 0
obeso = 0

for i in range(qtd_pessoas):
    sexo = input(f"Digite o sexo da pessoa {i+1}: ").lower()
    altura = float(input(f"Digite a altura da pessoa {i+1} [Ex: 1.65]: "))
    peso = float(input(f"Digite o peso da pessoa {i+1}: "))

    imc = peso/(altura*altura)
    imcs.append(imc)

    if (sexo == 'fm' and imc < 19.1 or imc < 20.7 ):
        abaixo += 1
    elif (sexo == 'fm' and imc >= 19.1 and imc < 25.8 or imc >= 20.7 and imc < 26.4):
        normal += 1
    elif (sexo == 'fm' and imc >= 25.8 and imc < 27.3 or imc >= 26.4 and imc < 27.8):
        p_acima += 1
    elif (sexo == 'fm' and imc >= 27.3 and imc < 31.1 or imc >= 27.8 and imc < 32.3):
        acima += 1
    else:
        obeso += 1

print("A quantidade de pessoas em cada nível de classificação é de: ")
print(f"Abaixo do peso: {abaixo}")
print(f"Peso normal: {normal}")
print(f"Um pouco acima do peso: {p_acima}")
print(f"Acima do peso: {acima}")
print(f"Obeso: {obeso}")
print(f"Todos os IMCs calculados: {imcs}")'''

#Questão 2
'''qtd_alunos = 0
nomeAluno = []
notaAluno = []

medias = 0

while (qtd_alunos != 3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    nomeAluno.append(nome)
    
    for n in nomeAluno:
        print("Nome Repetido")
        if (n in nomeAluno):
            nomeAluno.remove(n)
        
    if (nota > 10 or nota < 0):
        print("Nota inválida")
    else:
        notaAluno.append(nota)
    qtd_alunos += 1

while (True):
    print("Menu")
    print("Opção 1: Aluno com a maior e a menor nota")
    print("Opção 2: Informar a média geral da turma")
    print("Opção 3: Sair")

    op = int(input("Digite uma opção: "))

    if (op == 1):
        print(f"Aluno com a maior nota: {max(notaAluno)}")
        print(f"Aluno com a menor nota: {min(notaAluno)}")
        continue
    elif(op == 2):
        for m in notaAluno: 
            medias += m
        mediaGeral = medias/qtd_alunos
        print("Media Geral: ", mediaGeral)

        if (mediaGeral < 6):
            print("Situação Ruim")
        elif (mediaGeral >= 6 and mediaGeral <= 7):
            print("Situação Regular")
        elif (mediaGeral >= 7.1 and mediaGeral <= 8.9):
            print("Situação Boa")
        elif (mediaGeral >= 9 and mediaGeral <= 10):
            print("Situação Excelente")
        continue
    else:
        break'''

#Questão 3

'''print("Menu")
print("1. Cardápio")
print("2. Realizar Pagamento")
print("3. Sair")

cardapio = ["Cachorro Quente, Bauru Simples, Bauru com Ovo, Hambúrger, Cheesseburger, Refrigerante", 100, 101, 102, 103, 104, 105, 1.20, 1.30, 1.50, 1.20, 1.30, 1]
tot_pag = 0

while (True):
    opcao = int(input("Digite uma opção: "))

    if (opcao == 1):
        print("\n")
        print("Especificação   Código   Preço")
        print("Cachorro Quente  100     1,20")
        print("Bauru Simples    101     1,30")
        print("Bauru com Ovo    102     1,50")
        print("Hambúrger        103     1,20")
        print("Cheeseburger     104     1,30")
        print("Refrigerante     105     1,00")
        print("\n")

        item = int(input("Digite o código do item selecionado: "))
        qtd_item = int(input("Digite a quantidade: "))
        
        if (item == 100):
            tot_pag = 1.20*qtd_item
        elif (item == 101):
            tot_pag = 1.30*qtd_item
        elif (item == 102):
            tot_pag = 1.50*qtd_item
        elif (item == 103):
            tot_pag = 1.20*qtd_item
        elif(item == 104):
            tot_pag = 1.30*qtd_item
        elif (item == 105):
            tot_pag = 1*qtd_item
        continue
    elif (opcao == 2):
        valorTotal = tot_pag
        print(f"O valor total a ser pago é de: {valorTotal}")
    else:
        break'''