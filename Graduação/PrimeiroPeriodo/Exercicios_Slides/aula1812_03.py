'''Solicita o sexo e diz se é Feminino ou Masculino'''
sexo = input("Digite O seu sexo (F ou M): ")

if (sexo == "F" or sexo == "f"):
    print("Feminino")
elif (sexo == "M" or sexo == "m"):
    print("Masculino")
else:
    print("Inválido")