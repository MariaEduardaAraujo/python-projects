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
    for aluno in range(qtd_alunos):
        try:
            nome = input(f"Digite o nome do aluno {aluno+1}: ")
            print()
            
            if (nome.strip() == ""):
                print()
                print("É necessário digitar um nome!")
                continue
            
            nomeExiste = False
            for a in alunos:
                if(a[0] == nome):
                    nomeExiste = True
                    break
            if nomeExiste:
                print()
                print("Não é possível cadastrar nomes iguais!")
                continue

            
            notas = []
            for n in range(1, 5):
                while (True):
                    nota = float(input(f"Digite a nota {n} do aluno {nome}: "))
                    if(nota < 0 or nota > 10):
                        print()
                        print("Digite apenas números positivos e menores que 10!")
                    else:
                        notas.append(nota)
                        break

            alunos.append((nome, notas))
            print()
            print("Aluno cadastrado com suceso!")

                    
        except Exception as e:
            print()
            print("Ocorreu um erro!", e)
            continue
    print(alunos)
    print()

def removerNotas():
    try:
        nome = input("Digite o nome do aluno que você deseja remover as notas: ").strip()
        alunoLocalizado = False

        for a in alunos:
            if (a[0] == nome):
                alunoLocalizado = True
                
                try:
                    notaRemover = int(input("Qual nota [de 1 a 4] você deseja remover: "))
                    if (notaRemover < 1 or notaRemover > 4):
                        raise IndexError
                    
                    else:
                        notaRemover -= 1
                        a[1].pop(notaRemover)
                        
                        print()
                        print("Nota removida com sucesso!")
                        print(a)


                except IndexError:
                    print()
                    print("Índice fora do intervalo das notas!")
                    print("É necessário adicionar um valor de 1 a 4!")

        if not alunoLocalizado:
            print()
            print("Aluno não localizado!")

    except Exception as e:
        print()
        print("Ocorreu um erro!", e)

def substituirNotas():
    try:
        nome = input("Digite o nome do aluno que você deseja substituir as notas: ").strip()
        alunoLocalizado = False

        for a in alunos:
            if (a[0] == nome):
                alunoLocalizado = True
                
                try:
                    notaRemover = int(input("Qual nota [de 1 a 4] você deseja substituir: "))
                    if (notaRemover < 1 or notaRemover > 4):
                        raise IndexError("Índice fora do intervalo das notas!")
                    else:
                        notaRemover -= 1
                        a[1].pop(notaRemover)

                        novaNota = float(input("Digite a nota nota: "))
                        if (novaNota < 0 or novaNota > 10):
                            print()
                            raise ValueError
                        else:
                            a[1].insert(notaRemover, novaNota)
                            print()
                            print("Nota substituida com sucesso!")
                            print(a)

                except ValueError:
                    print()
                    print("Digite apenas números positivos e menores que 10!")

        if not alunoLocalizado:
            print()
            print("Aluno não localizado!")

    except Exception as e:
        print()
        print("Ocorreu um erro!", e)

def calcularResultado():
    try:
        for a in alunos:
            media = sum(a[1]) / 4
            if (media >= 6):
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
        if (menu <= 0):
            raise ValueError
    except ValueError:
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