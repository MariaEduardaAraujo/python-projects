def menu():
    print('''Criar Evento
a. Criar Evento
b. Criar lista de Convidados
c. Sair''')

evento = []
eventoConvidados = []

while(True):
    menu()
    opcao1 = input("Qual opção você deseja? ").upper()
    
    if(opcao1 == "A"):
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
        
    elif (opcao1 == "B"):
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
                
            opcao3 = input("Deseja adicionar mais uma pessoa ao evento? [sim/nao] ").upper()
            if(opcao3 == "SIM"):
                quit #Não Func
            else:
                exit
        else:
            print("Informação Inválida!")
            continue

    elif(opcao1 == "C"):
        break
    else:
        print("Informação Inválida!")
        continue
