cliente = []
nomedoanimal = []
tipoanimal = []
banho = 50
tosa = 40
veterinario = 30
bt = 75
soma = []

dono = input('Nome do cliente: ')
tipo = input("Tipo do animal: ")
nome = input('Nome do animal: ')
cliente.append(dono)
nomedoanimal.append(nome)

print('''Pet Shop IFALZÃO
            1- Servirços:
                1.2 - Banho
                1.3 - Tosa
                1.4 - Banho e tosa
                1.5 - Veterinário
                1.6 - Valor Total
            2 - Sair''')

opcao = eval(input('Opção desejada: '))

def servico():
    serv = eval(input('Serviço desejado: '))
    if serv == 1.2:
        opb = banho
        print('Sr.(a)', cliente, 'seu animal de estimação é: ', nome , 'classificado como: ', tipo)
        soma.append(opb)
        print("preço a pagar: ",soma)
    elif serv == 1.3:
        opt = tosa
        print('Sr.(a)', cliente, 'seu animal de estimação é: ', nome , 'classificado como: ', tipo)
        soma.append(opt)
        print("preço a pagar: ", soma)
    elif serv == 1.4:
        opbt = bt
        print('Sr.(a)', cliente, 'seu animal de estimação é: ', nome , 'classificado como: ', tipo)
        soma.append(opbt)
        print("preço a pagar: ", soma)
    elif serv == 1.5:
        opv = veterinario
        print('Sr.(a)', cliente, 'seu animal de estimação é: ', nome , 'classificado como: ', tipo)
        soma.append(opv)
        print("preço a pagar: ", soma)
    elif serv == 1.6:
       print('Obrigado por usar nossos serviços! Até mais!')
       print('Total gasto: ', sum(soma))

while opcao!= 2:
    if opcao==1:
        servico()
    else:
        print('Obrigado por usar nossos serviços! Até mais!')
    opcao = eval(input('Opção desejada: '))
