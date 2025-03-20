#Aula 17/03/2025

from PilhaArray import *

pilha = PilhaArray()

print("Adicionando")
pilha.push(5)
pilha.push(9)
pilha.push(13)

print("\nVerificando tamanho")
print(pilha.size())
print(len(pilha))

print("\nVerificando topo")
print(pilha.top())


#Inverter texto
print("\nInvertendo texto")

def inverte_texto(texto):
    pilha = PilhaArray()
    for letra in texto:
        pilha.push(letra)

    palavra = ""
    while not pilha.is_empty():
        palavra += pilha.pop()
    return palavra

texto = "Aprendendo Python"
print(inverte_texto(texto))

#Verificando Delimitadores e Tags
print("\nVerificando Delimitadores")
def is_matched(expr):
    abre = '({['
    fecha = ')}]'
    pilha = PilhaArray()
    for d in expr:
        if d in abre:
            pilha.push(d)
        elif d in fecha:
            if pilha.is_empty():
                return False
            if fecha.index(d) != abre.index(pilha.pop()):
                return False
    return pilha.is_empty()
    
print(is_matched("({[])}"))