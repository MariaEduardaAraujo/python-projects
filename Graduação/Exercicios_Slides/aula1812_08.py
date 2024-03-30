'''Solicita as notas e calcula a média'''

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
bomComportamento = input("O aluno tem bom comportamento? (S ou N) ")

media = (nota1+nota2)/2

if (media < 4.0):
    print(f"Reprovado por média {media}")
elif (media >= 4.1 and bomComportamento == "S" or bomComportamento == "s"):
    print(f"Recuperção por média {media}")
elif (media >= 6.0):
    print(f"Aprovado com média {media}")