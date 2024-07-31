#Recuperação
#Davi e Maria Eduarda

'''Q3. Inscrever Participante (1,0 / 2,0)
- A verificação de existência do evento e a verificação de capacidade cheia não estão 
funcionando adequadamente.
- O código entra em um loop desnecessário quando o evento não existe.'''

eventos = []
participantes = [] 
cp = 0
venda = 0

def menu():
    print("1. Cadastrar Evento");
    print("2. Inscrever Partipante");
    print("3. Listar inscritos para evento");
    print("4. Remover inscrição para evento");
    print("5. Relatório de Arrecadação");
    print("6. Sair");
    print()

def cadastrarEvento():
    global cp
    global venda
    try:
        while(True):
            nome = input("Digite o nome do evento: ").strip()
            valor = float(input("Digite o valor do ingresso: "))
            capacidade = int(input("Digite a capacidade do evento: "))

            if (nome == ""):
                print("É necessário digitar um nome! Tente novamente")
                print()
                continue
                
            if (valor < 1):
                print("O valor do ingresso não pode ser menor que 1 real! Tente novamente")
                print()
                continue
            
            if (capacidade < 10):
                print("A capacidade do evento deve ser maior que 10! Tente novamente")
                print()
                continue

            eventoExiste = False
            for e in eventos:
                if (e[0] == nome):
                    eventoExiste = True
                    break

            if eventoExiste:
                print("Não é possível cadastrar eventos com o mesmo nome! Tente novamente")
                print()
                continue
            
            eventos.append((nome, valor, capacidade))
            print("Evento cadastrado com sucesso!")
            print(eventos)
            print()
            break

    except ValueError:
        print("Os valores têm que ser números inteiros e positivos")
        print()

def inscreverParticipante():
    global cp
    global venda
    try:
        while(True):
            for e in eventos:
                print(f" - {e[0]}");
            
            if (len(eventos) <= 0):
                print("Primeiro cadastre um evento para prosseguirmos!")
                print()
                return
            
            escolha_evento = input("Digite o evento que deseja escolher: ");
            print()

            for e in eventos:
                if (escolha_evento != e[0]):
                    print("Evento inexistente! Tente novamente");
                    print()
                    continue

                elif (e[2] == 0):
                    print("Capacidade do evento está lotada! Escolha outro evento.");
                    print()
                    break
                else:
                    nome = input("Digite seu nome: ").strip()
                    cpf = int(input("Digite o seu CPF: "));
            
            if (nome == ""):
                print("Nome vazio! É necessário digitar um nome. Tente novamente!")
                continue

            participanteExiste = False
            for p in participantes:
                if (p[0] == nome):
                    participanteExiste = True
                    break
                elif (p[1] == cpf):
                    print("CPF já cadastrado! Por favor, digite novamente.")
                    print()
                    continue

            if (participanteExiste):
                print("Nome já cadastrado! Por favor, digite novamente.");
                print()
                continue
            else:
                participantes.append((nome, cpf, e))
                print("Cadastro feito com sucesso no evento!")
                print()
                cp += 1
            break      
    except ValueError:
        print("É necessário digitar um valor inteiro e positivo! Tente novamente")
        print()

    except Exception as e:
        print("Ocorreu um erro")
        print(e)
        print()

def listarInscritos():
    for p in participantes:
        if (len(p) <= 0):
            print("É necessário cadastrar um evento! Tente novamente")
        else:
            while(True):
                print(f" - {p[2][0]}");
                
                eventoEscolhido = input("Escolha o título do evento que deseja listar: ")
                for e in eventos:
                    if (e[0] == eventoEscolhido):
                        print(f"** Inscritos no evento {e[0]} **")
                        print(f"Quantidade de inscritos: {e[2]}")
                        print(f"Informações sobre os inscritos")
                        for p in participantes:
                            if (len(p) > 0):
                                print(f"Nome: {p[0]}")
                                print(f"CPF: {p[1]}")
                        print()
                    
                    else:
                        print("Evento não localizado. Tente novamente!")
                        continue
                break
def removerInscricao():
    try:
        for ep in participantes:
            if (len(ep) > 0):
                print(f"Lista de eventos que possuem participantes:")
                print(f"- {ep[2][0]}")
            else:
                print("Ainda não há participantes cadastrados nos eventos! Tente novamente")

        eventoEscolhido = input("Escolha um evento para continuar: ")
        for ep in participantes:
            if (ep[2][0] != eventoEscolhido):
                print("Evento não localizado! Tente novamente!")
                continue
            else:
                for p in participantes:
                    print(f"- {p[:2]}")
                    cpfRemover = int(input("Digite o CPF que você quer remover: "))
                    if (p[1] == cpfRemover):
                        participantes.remove(p)
                        print("CPF removido com sucesso!")
                        print()
                    else:
                        print("O CPF digitado não foi encontrado. Tente novamente!")
                        print()
    except ValueError:
        print("É necessário digitar um valor inteiro e positivo! Tente novamente")
        print()
    except Exception as e:
        print("Ocorreu um erro")
        print(e)
        print()


def relatorioArrecadacao():
    for a in eventos:
        print(f"O evento {a[0]}, vendeu {cp} ingresso(s)");
        venda = cp*a[1]
        print(f"Totalizando: {venda} reais")
        print()

while (True):
    menu()
    try:
        escolha_menu = int(input("Escolha uma das opções: "));
        if (escolha_menu < 1 or escolha_menu > 6):
            print("Digite apenas valores entre 1 e 5")
            continue
    except ValueError:
        print("É necessário digitar um valor inteiro e positivo! Tente novamente")
        print()
    
    if (escolha_menu == 1):
        cadastrarEvento()
    elif (escolha_menu == 2):
        inscreverParticipante()
    elif (escolha_menu == 3):
        listarInscritos()
    elif (escolha_menu == 4):
        removerInscricao()
    elif (escolha_menu == 5):
        relatorioArrecadacao()
    elif (escolha_menu == 6):
        print("Saindo...")
        break
