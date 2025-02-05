#Faça um script Python que, dados os coeficientes de uma equação do 2° grau A, B, C ,calcula as raízes dessa equação.
import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = b**2 - 4*a*c
raiz1 = (-b + math.sqrt(delta))/(2*a)
raiz2 = (-b - math.sqrt(delta))/(2*a)

print(f"A raiz 1 é: {raiz1}")
print(f"A raiz 2 é: {raiz2}")   

