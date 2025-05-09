def hash_val(chave, tamanho): #Questão 3
        return chave % tamanho

def hashing(): #Questão 5
        tabela = [None]*7
        chave = 20
        indice = chave % len(tabela)
        tabela[indice] = "valor"
        print(tabela)

tamanho = 10
print(hash_val(25, tamanho))
print(hashing())