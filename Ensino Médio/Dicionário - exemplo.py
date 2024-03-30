pets = []
maior = ' '
opcao = int(input('Opção: '))

def cadastro():
    pet = {}
    pet ["Nome"] = input('Nome do pet: ')
    pet ["Raça"] = input('Raça do pet: ')
    pet ["Valor"] = float(input('Valor atribuído: '))
    maior = max(pet.get("Valor"))
    pets.append(pet)
    print(pets)
    
def maiorvalor():
    print('Maior valor: ', maior)

while opcao!=3:
    if opcao==1:
        cadastro()
    elif opcao==2:
        maiorvalor()
    opcao = int(input('Opção: '))
