#Casting = conversao de tipos!
'''
qtd_pessoas = int(input("Qual a quantidade de pessoas? "));

lista_imc_calculados = [];

lista_abaixo_peso = [];
lista_peso_ideal = [];
lista_um_pouco_acima_peso = [];
lista_acima_peso_ideal = [];
lista_obesos = [];

for i in range(0, qtd_pessoas):
    sexo = input("Qual o sexo? (M - Masculino, F - Feminino) ").upper();
    altura = float(input("Qual a altura? "));
    peso = float(input("Qual o peso? "));

    imc = peso / (altura * altura);
    lista_imc_calculados.append(imc);

    if(sexo == "F"):
        if(imc < 19.1):
            print(">> Abaixo do peso");
            lista_abaixo_peso.append(imc);
        elif(imc < 25.8):
            print(">> Peso ideal");
            lista_peso_ideal.append(imc);
        elif(imc < 27.3):
            print(">> Um pouco acima do peso");
            lista_um_pouco_acima_peso.append(imc);
        elif(imc < 31.1):
            print(">> Acima do peso ideal");
            lista_acima_peso_ideal.append(imc);
        else:
            print(">> Obeso");
            lista_obesos.append(imc);
    elif(sexo == "M"):
        if(imc < 20.7):
            print(">> Abaixo do peso");
            lista_abaixo_peso.append(imc);
        elif(imc < 26.4):
            print(">> Peso ideal");
            lista_peso_ideal.append(imc);
        elif(imc < 27.8):
            print(">> Um pouco acima do peso");
            lista_um_pouco_acima_peso.append(imc);
        elif(imc < 32.3):
            print(">> Acima do peso ideal");
            lista_acima_peso_ideal.append(imc);
        else:
            print(">> Obeso");
            lista_obesos.append(imc);
        input();

print();
print(f"Pessoas abaixo do peso: {len(lista_abaixo_peso)}");
print(f"Pessoas com peso ideal: {len(lista_peso_ideal)}");
print(f"Pessoas um pouco acima do peso: {len(lista_um_pouco_acima_peso)}");
print(f"Pessoas acima do peso: {len(lista_acima_peso_ideal)}");
print(f"Pessoas obesas: {len(lista_obesos)}");

print();
print("IMCs calculados: ");
for i in lista_imc_calculados:
    print(f"{i:.2f}");'''

#Questão 2
'''
qtd_alunos = 3;
cont = 0;
lista_nomes = [];
lista_notas = [];
maior_nota = 0;
menor_nota = 99;
somas_notas = 0;

while(cont < qtd_alunos):
    nome = input(f"Qual o nome do aluno {cont+1}? ");

    if(len(lista_nomes) == 0):
        lista_nomes.append(nome);
    else:
        if(nome in lista_nomes):
            print("Nome já foi digitado antes");
            continue;
        else:
            lista_nomes.append(nome);

    while(True):
        nota = float(input(f"Qual a nota do estudante {cont+1}? "));

        if(nota < 0 or nota > 10):
            print("Nota inválida");
            continue;
        else:
            somas_notas += nota;
            lista_notas.append(nota);
            
            if(nota > maior_nota):
                maior_nota = nota;
            
            if(nota < menor_nota):
                menor_nota = nota;
            
            break;
    cont += 1;

escolha = 0;

while(escolha != 3): 
    print("Menu");
    print("1 - Exibir a maior e menor nota");
    print("2 - Exibir a média geral da turma");
    print("3 - Sair");
    escolha = int(input("Escolha uma opção: "));

    if(escolha == 1):
        print(f"Maior nota: {maior_nota}");
        print(f"Menor nota: {menor_nota}");
    elif(escolha == 2):
        media_geral = somas_notas/qtd_alunos;
        print(f"Média geral da turma: {media_geral}");
        
        if(media_geral < 6):
            print("Classificação da turma: ruim");
        elif(media_geral < 7.1):
            print("Classificação da turma: regular");
        elif(media_geral < 9):
            print("Classificação da turma: boa");
        elif(media_geral <= 10):
            print("Classificação da turma: excelente");
        input();
    elif(escolha == 3):
        print("Encerrando...");
    else:
        print("Opção inválida");
        input();
cont = 0;
lista_nomes = [];
lista_notas = [];
maior_nota = 0;
menor_nota = 99;
somas_notas = 0;

while(cont < qtd_alunos):
    nome = input(f"Qual o nome do aluno {cont+1}? ");

    if(len(lista_nomes) == 0):
        lista_nomes.append(nome);
    else:
        if(nome in lista_nomes):
            print("Nome já foi digitado antes");
            continue;
        else:
            lista_nomes.append(nome);

    while(True):
        nota = float(input(f"Qual a nota do estudante {cont+1}? "));

        if(nota < 0 or nota > 10):
            print("Nota inválida");
            continue;
        else:
            somas_notas += nota;
            lista_notas.append(nota);
            
            if(nota > maior_nota):
                maior_nota = nota;
            
            if(nota < menor_nota):
                menor_nota = nota;
            
            break;
    cont += 1;

escolha = 0;

while(escolha != 3): 
    print("Menu");
    print("1 - Exibir a maior e menor nota");
    print("2 - Exibir a média geral da turma");
    print("3 - Sair");
    escolha = int(input("Escolha uma opção: "));

    if(escolha == 1):
        print(f"Maior nota: {maior_nota}");
        print(f"Menor nota: {menor_nota}");
    elif(escolha == 2):
        media_geral = somas_notas/qtd_alunos;
        print(f"Média geral da turma: {media_geral}");
        
        if(media_geral < 6):
            print("Classificação da turma: ruim");
        elif(media_geral < 7.1):
            print("Classificação da turma: regular");
        elif(media_geral < 9):
            print("Classificação da turma: boa");
        elif(media_geral <= 10):
            print("Classificação da turma: excelente");
        input();
    elif(escolha == 3):
        print("Encerrando...");
    else:
        print("Opção inválida");
        input();
'''