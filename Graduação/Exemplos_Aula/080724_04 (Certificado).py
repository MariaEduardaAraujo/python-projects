def menu():
    print('''Criar Evento
1. Criar Evento
2. Criar lista de Convidados
3. Registrar Presença
4. Emitir Certificado
5. Sair''')

evento = []
eventoConvidados = []

while (True):
    menu()
    opcao1 = int(input("Qual opção você deseja? "))
    
    if (opcao1 == 1):
        print("Módulo de Criação de Eventos")
        print("Digite os seguintes dados: ")
        
        data = input("Digite a data: [DD/MM/AA] ")
        titulo = input("Digite o título do evento: ")
        local = input("Digite o local do evento: ")
        capacidade = int(input("Digite a capacidade do evento: "))

        eventoExistente = False
        for ev in evento:
            if (ev[0] == data and ev[1] == titulo):
                eventoExistente = True
                
        if not eventoExistente:
            evento.append((data, titulo, local, capacidade))
            print(f"O evento {titulo} a ser realizado no local {local} no dia {data} foi cadastrado com sucesso.")
            continue
        else:
            print("O seu evento não foi criado. Tente novamente.")
            continue
        
    elif (opcao1 == 2):
        print("Módulo de Criação de Eventos")
        print("Eventos cadastrados: ")
        for ev in evento:
           print(f"- {ev[1]}")

        opcao2 = input("Em qual evento você deseja adicionar um convidado: ")

        if (opcao2 in ev):
            nome = input("Qual é o nome do participante? ")

            if (nome == ""):
                print("É necessário digitar um nome")
                continue
            else:
                if(nome in eventoConvidados):
                    print("Não é possível adicionar pessoas com o mesmo nome")
                    continue
                else:
                    eventoConvidados.append(nome)
                    print("Pessoa adicionada com sucesso!")

        else:
            print("Informação Inválida!")
            continue

        opcao3 = input("Deseja adicionar mais uma pessoa ao evento? [sim/nao] ").upper()
        if (opcao3 == "SIM"):
            continue #Não Func
        else:
            exit

    elif (opcao1 == 3):
        print("Módulo de Registro de Presença")
        print("Eventos cadastrados: ")
        for ev in evento:
           print(f"- {ev[1]}")

        opcao4 = input("Em qual evento você deseja registrar presenças: ")

        if (opcao2 in ev):
            nome = input("Qual é o nome do participante? ")
            if (nome == ""):
                print("É necessário digitar um nome")
                continue
            else:
                if (nome in eventoConvidados):
                    print("Presença registrada com sucesso")
                else:
                    print("Presença não confirmada")
                    exit
        else:
            print("Informação Inválida!")
            continue
        opcao5 = input("Deseja confirmar mais uma presença? [sim/nao] ").upper()
        if (opcao3 == "SIM"):
            quit #Não Func
        else:
            exit

    elif (opcao1 == 4):
        print(":)")

    elif (opcao1 == 5):
        break
    
    else:
        print("Informação Inválida!")
        continue