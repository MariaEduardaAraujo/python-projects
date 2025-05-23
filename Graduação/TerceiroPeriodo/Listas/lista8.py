#Lista de Exercícios 08 (Pesquisa)

#Questão 9
'''def busca_bin_str(palavra, valor):
    inicio, fim = 0, len(palavra)-1

    while inicio <= fim:
        meio = (inicio + fim)//2
        
        if palavra[meio] == valor:
            return meio
        elif valor < palavra[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
   
    return -1

lista = ["apple", "banana", "cherry", "guava", "mango"]
valor = "mango"
print(busca_bin_str(lista, valor))'''

#Questão 11
'''def busca_bin_recursiva(lista, valor):
    if len(lista) == 0:
        return False
    
    meio = len(lista)//2
    if lista[meio] == valor:
        return True
    else:
        if valor < lista[meio]: return busca_bin_recursiva(lista[:meio], valor)
        else: return busca_bin_recursiva(lista[meio+1:], valor)

lista = [2, 4, 6, 8, 10, 12, 14]
valor = 8
print(busca_bin_recursiva(lista, valor))'''

#Questão 12
'''def pesquisa_binaria(lista, valor):
    qtd = []
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            qtd.append(meio)
            
            esquerda = meio - 1
            while esquerda >= 0 and lista[esquerda] == valor:
                qtd.append(esquerda)
                esquerda -= 1

            direita = meio + 1
            while direita < len(lista) and lista[direita] == valor:
                qtd.append(direita)
                direita += 1

            return sorted(qtd)

        else:
            if lista[meio] < valor: 
                inicio = meio + 1
            else: 
                fim = meio - 1
                
    return -1
    
lista = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9,]
valor = 8
print(pesquisa_binaria(lista, valor))'''

#Questão 13
'''def busca_bin_recursiva(lista, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1

    if inicio > fim:
        return False
    
    meio = (inicio+fim)//2
    if lista[meio] == valor:
        return meio
    else:
        if valor < lista[meio]: return busca_bin_recursiva(lista, valor, inicio, meio-1)
        else: return busca_bin_recursiva(lista, valor, meio+1, fim)

lista = [2, 4, 6, 8, 10, 12, 14]
valor = 8
print(busca_bin_recursiva(lista, valor))'''

#Questão 14
'''def busca_bin_slice(lista, valor):
    if len(lista) == 0:
        return False
    
    meio = len(lista)//2
    if lista[meio] == valor:
        return True
    else:
        if valor < lista[meio]: return busca_bin_recursiva(lista[:meio], valor)
        else: return busca_bin_recursiva(lista[meio+1:], valor)

def busca_bin_recursiva(lista, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1

    if inicio > fim:
        return False
    
    meio = (inicio+fim)//2
    if lista[meio] == valor:
        return meio
    else:
        if valor < lista[meio]: return busca_bin_recursiva(lista, valor, inicio, meio-1)
        else: return busca_bin_recursiva(lista, valor, meio+1, fim)

lista = [343, 473, 90, 126, 448]
lO = lista.sort()

valor = 473
print(busca_bin_recursiva(lista, valor))
print(busca_bin_recursiva(lista, valor))'''