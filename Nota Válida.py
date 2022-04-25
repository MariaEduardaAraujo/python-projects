##nota = int(input("Digite uma nota entre 0 e 10: "))
##
##while nota >10 or nota < 0:
##    print("Nota inválida")
##    nota = int(input("Digite uma nota entre 0 e 10: "))

nomeDeUsuario = str(input("Nome de Usuário: "))
senha = str(input("Senha: "))

while senha == nomeDeUsuario:
    print("Senha inválida")
    nomeDeUsuario = str(input("Nome de Usuário: "))
    senha = str(input("Senha: "))
