#Davi e Maria Eduarda

alunos = []

def inicializacao():
    print("** SISTEMA DE NOTAS **\n");
    print("1. Inserir notas ");
    print("2. Remover notas ");
    print("3. Substituir notas");
    print("4. Calcular resultado final");
    print("5. Sair");
    print()

def inserirNotas():
    print("Inserir Notas")
    for i in range(qtd_alunos):
        try:
            nome = input(f"Digite o nome do aluno {i+1}: ")
            print()
            if (nome.strip() == ""):
                print("É necessário digitar um nome!")
                print()
                continue
            
            nomeExiste = False
            for a in alunos:
                if(a[0] == nome):
                    nomeExiste = True
                    alunos.pop()
                    continue #Não Funciona
            if not nomeExiste:
                try:
                    nota1 = float(input(f"Digite a nota {1} do aluno: "))
                    nota2 = float(input(f"Digite a nota {2} do aluno: "))
                    nota3 = float(input(f"Digite a nota {3} do aluno: "))
                    nota4 = float(input(f"Digite a nota {4} do aluno: "))
                    
                    if (nota1 == "" or nota2 == "" or nota3 == "" or nota4 == ""):
                        print("É necessário digitar todas as notas!")
                        print()
                        continue
                    else:
                        alunos.append((nome, [nota1, nota2, nota3, nota4]))
                        
                        print("Aluno cadastrado com suceso!")
                        print()
                        
                except ValueError:
                    print("Digite apenas números positivos!")
                    print()
                    continue
            else:
                print("Não é possível cadastrar nomes iguais!")
                print()
                continue
        except Exception as e:
            print("Ocorreu um erro!", e)
            print()

def removerNotas():
    try:
        nome = input("Digite o nome do aluno que você deseja remover as notas: ")
        for a in alunos:
            if (a[0] == nome):
                notaRemover = int(input("Qual nota [de 1 a 4] você deseja remover: "))
                if (notaRemover == "" or notaRemover > 4):
                    raise Exception("É necessário adicionar um valor de 1 a 4!")
                else:
                    indice = notaRemover - 1
                    for n in alunos:
                        for i in n[1]:
                            if (len(i) == indice):
                                alunos.remove(i[indice])
                                print("Nota removida")
                                print()
                            else:
                                raise Exception
            else:
                print("Aluno não localizado")
                print()
    except ValueError:
        print("Digite apenas números inteiros e positivos!")
        print()
    except Exception:
        print("Indice não localizado")
        print()

def substituirNotas():
    try:
        nome = input("Digite o nome do aluno que você deseja substituir as notas: ")
        for a in alunos:
            if (a[0] == nome):
                notaSubstituir = int(input("Qual nota [de 1 a 4] você deseja substituir: "))
                if (notaSubstituir == "" or notaSubstituir > 4):
                    raise Exception("É necessário adicionar um valor de 1 a 4!")
                else:
                    indice = notaSubstituir - 1
                    for n in alunos:
                        for i in n[1]:
                            if (len(i) == indice):
                                novaNota = float(input("Digite a nova nota: "))
                                alunos.append(novaNota)
                                print("Nota Substituida")
                                print()
                            else:
                                raise Exception
            else:
                print("Aluno não localizado")
                print()
    except ValueError:
        print("Digite apenas números inteiros e positivos!")
        print()
    except Exception:
        print("Indice não localizado")
        print()

def calcularResultado():
    try:
        soma = 0
        media = 0
        for n in alunos:
            for i in n[1]:
                soma = soma + i
                media = soma/4

        for a in alunos:
            if (soma >= 6):
                print(f"O aluno {a[0]} foi Aprovado com média: {media}")
                print()
            else:
                print(f"O aluno {a[0]} foi Reprovado com média: {media}")
                print()
    except Exception as e:
        print("Ocorreu um erro", e)


while(True):
    try:
        print("Tela de Configuração")
        qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
        if (qtd_alunos <= 0):
            raise ValueError
        else:
            print()
            break
    except ValueError:
        print("Digite apenas números inteiros e positivos!")
        continue

while(True):
    inicializacao()
    try:
        menu = int(input("Escolha uma opção: "));
    except:
        print("Digite apenas números inteiros e positivos [de 1 a 5]!")
        print()
    try:    
        if (menu == 1):
            inserirNotas();
        elif (menu == 2):
            removerNotas();
        elif (menu == 3):    
            substituirNotas();
        elif (menu == 4):
            calcularResultado();
        elif (menu == 5):
            print("Saindo...");
            break
    except:
        print("Valor fora dos padrões estabelecidos. Redigite sua opção!");
        print()
    