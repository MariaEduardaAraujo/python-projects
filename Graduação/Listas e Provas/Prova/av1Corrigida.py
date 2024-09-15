# Maria Eduarda e Raphael

#Questao 1 Corrigida
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

    if (sexo == 'f'):
        if (imc < 19.1):
            print(">> Abaixo do peso")
            abaixo += 1
        elif (sexo == 'f' and imc >= 19.1 and imc < 25.8):
            print(">> Peso ideal")
            normal += 1
        elif (sexo == 'f' and imc >= 25.8 and imc < 27.3):
            print(">> Um pouco acima do peso")
            p_acima += 1
        elif (sexo == 'f' and imc >= 27.3 and imc < 31.1):
            print(">> Acima do peso ideal")
            acima += 1
        else:
            print(">> Obesa")
            obeso += 1

    elif (sexo == 'm'):
        if(imc < 20.7 ):
            print(">> Abaixo do peso")
            abaixo += 1
        elif (sexo == 'm' and imc >= 20.7 and imc < 26.4):
            print(">> Peso ideal")
            normal += 1
        elif (sexo == 'm' and imc >= 26.4 and imc < 27.8):
            print(">> Um pouco acima do peso")
            p_acima += 1
        elif (sexo == 'm' and imc >= 27.8 and imc < 32.3):
            print(">> Acima do peso ideal")
            acima += 1
        else:
            print(">> Obeso")
            obeso += 1

print("A quantidade de pessoas em cada nível de classificação é de: ")
print(f"Abaixo do peso: {abaixo}")
print(f"Peso ideal: {normal}")
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
    
    if(len(nomeAluno) == 0):
        nomeAluno.append(nome)
    else:
        if(nome in nomeAluno):
            print("Nome já foi digitado antes")
            continue
        else:
            nomeAluno.append(nome)

    while(True):
        nota = float(input(f"Qual a nota do aluno: "))

        if(nota < 0 or nota > 10):
            print("Nota inválida")
            continue
        else:
            notaAluno.append(nota);
            break;
    qtd_alunos += 1

while (True):
    print("Menu")
    print("Opção 1: Aluno com a maior e a menor nota")
    print("Opção 2: Informar a média geral da turma")
    print("Opção 3: Sair")

    op = int(input("Digite uma opção: "))

    if (op == 1):
        print(f"Maior nota: {max(notaAluno)}")
        print(f"Menor nota: {min(notaAluno)}")
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
        print("Saindo...")
        break'''

#Questão 3
'''print("=== Menu ===")
print("1. Cardápio")
print("2. Realizar Pagamento")
print("3. Sair")
print()

cardapio = [["Cachorro Quente", 100, 1.20], ["Bauru Simples", 101, 1.30], ["Bauru com Ovo", 102, 1.50], ["Hambúrger", 103, 1.20], ["Cheesseburger", 104, 1.30], ["Refrigerante", 105, 1]]
tot_pag = 0

while (True):
    opcao = int(input("Digite uma opção: "))

    if (opcao == 1):
        print()
        print("Especificação   Código   Preço")
        for i in cardapio:
            print(i)
        print("=" * 30)
        print()

        item = int(input("Digite o código do item selecionado: "))
        qtd_item = int(input("Digite a quantidade: "))
        
        for i in cardapio:
            if item in i:
                if (item == 100):
                    tot_pag = tot_pag+(1.20*qtd_item)
                elif (item == 101):
                    tot_pag = tot_pag+(1.30*qtd_item)
                elif (item == 102):
                    tot_pag = tot_pag+(1.50*qtd_item)
                elif (item == 103):
                    tot_pag = tot_pag+(1.20*qtd_item)
                elif(item == 104):
                    tot_pag = tot_pag+(1.30*qtd_item)
                elif (item == 105):
                    tot_pag = tot_pag+(1*qtd_item)
                else:
                    print("Valor inválido")
                    continue
        print("=" * 30)
            
    elif (opcao == 2):
        valorTotal = tot_pag
        print()
        print(f"O valor total a ser pago é de: {valorTotal}")
        print("=" * 30)
    else:
        print("Saindo...")
        break'''