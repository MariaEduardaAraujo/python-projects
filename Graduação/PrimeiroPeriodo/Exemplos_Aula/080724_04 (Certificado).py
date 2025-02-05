def menu():
    print('''Criar Evento
1. Criar Evento
2. Criar lista de Convidados
3. Registrar Presença
4. Emitir Certificado
5. Sair''')

evento = []
eventoConvidados = []
presenca = []

while (True):
    print()
    menu()
    print()
    opcao1 = int(input("Qual opção você deseja? "))
    
    if (opcao1 == 1):
        print()
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
            print()
            print(f"O evento {titulo} a ser realizado no local {local} no dia {data} foi cadastrado com sucesso.")
            continue
        else:
            print()
            print("O seu evento não foi criado. Tente novamente.")
            continue
        
    elif (opcao1 == 2):
        while(True):
            print()
            print("Módulo de Criação de Eventos")
            print("Eventos cadastrados: ")
            for ev in evento:
                print(f"- {ev[1]}")

                addConvidado = input("Em qual evento você deseja adicionar um convidado: ")

                if (addConvidado in ev):
                    nome = input("Qual é o nome do participante? ")

                    if (nome == ""):
                        print()
                        print("É necessário digitar um nome")
                        continue
                    else:
                        if(nome in eventoConvidados):
                            print()
                            print("Não é possível adicionar pessoas com o mesmo nome")
                            continue
                        else:
                            eventoConvidados.append(nome)
                            print()
                            print("Pessoa adicionada com sucesso!")

                else:
                    print("Informação Inválida!")
                    continue
            
            print()
            addConvidado2 = input("Deseja adicionar mais uma pessoa ao evento? [sim/nao] ").upper()
            if (addConvidado2 == "SIM"):
                continue
            else:
                break

    elif (opcao1 == 3):
        while(True):
            print()
            print("Módulo de Registro de Presença")
            print("Eventos cadastrados: ")
            for ev in evento:
                print(f"- {ev[1]}")

                presenca = input("Em qual evento você deseja registrar presenças: ")

                if (presenca in ev):
                    nome = input("Qual é o nome do participante? ")
                    if (nome == ""):
                        print()
                        print("É necessário digitar um nome")
                        continue
                    else:
                        if (nome in eventoConvidados):
                            print()
                            print("Presença registrada com sucesso")
                        else:
                            print()
                            print("Presença não confirmada")
                            exit
                else:
                    print("Informação Inválida!")
                    continue
            
            print()
            confPresenca = input("Deseja confirmar mais uma presença? [sim/nao] ").upper()
            if (confPresenca == "SIM"):
                continue
            else:
                break

    elif (opcao1 == 4):
        print()
        print("Módulo de Registro de Presença")
        print("Eventos cadastrados: ")
        for ev in evento:
            print(f"- {ev[1]}")

            certEvento = input("Em qual evento você deseja emitir certificados: ")

            if (certEvento in ev):
                for c in eventoConvidados:
                    print(f"Certifico que {c} participou do {ev[1]} no dia {ev[0]}, realizado no {ev[2]}.")
                break
            else:
                print("O evento pesquisado não foi encontrado. Verifique novamente.")

    elif (opcao1 == 5):
        print("Saindo...")
        break
    
    else:
        print("Informação Inválida!")
        continue