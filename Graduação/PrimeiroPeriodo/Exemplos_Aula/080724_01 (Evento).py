def menu():
    print('''Criar Evento
a. Criar Evento
b. Sair''')

def tamanhoLista(lista):
    return len(evento)

evento = []

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

        if (tamanhoLista(evento) <= 0):
            evento.append((data, titulo, local, capacidade))
            print(f"O evento {titulo} a ser realizado no {local} no dia {data} foi cadastrado com sucesso.")
            exit
        else: 
            for ev in evento:
                if (ev == data or ev == titulo):
                    print("O seu evento não foi criado. Tente novamente. ")
                    break
                else:
                    evento.append((data, titulo, local, capacidade))
                    print(f"O evento {titulo} a ser realizado no local {local} no dia {data} foi cadastrado com sucesso.")
                    break
            
    elif(opcao1 == "B"):
        break
    else:
        print("Informação Inválida!")
        continue
