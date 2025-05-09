from Noh import *

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.qtd = 0

    def add(self, e): #Adiciona no começo
        temp = Noh(e)
        temp.setNext(self.head)
        self.head = temp
        self.qtd += 1
    
    def append(self, e): #Adiciona no fim, Questão 1
        novo = Noh(e)
        self.qtd += 1

        if self.head is None:
            self.head = novo
            return
        
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo

    def insert(self, p, e): #Questão 1
        novo = Noh(e)
        self.qtd += 1

        if self.head is None: 
            self.head = novo
            return

        if p <= 0:
            novo.proximo = self.head
            self.head = novo
            return

        i = 0
        atual = self.head

        while atual.proximo is not None and i < p - 1:
            atual = atual.proximo
            i += 1

        novo.proximo = atual.proximo
        atual.proximo = novo

    def pop(self): #Questão 1
        atual = self.head
        anterior = None
        self.qtd -= 1

        while atual.proximo is not None:
            anterior = atual
            atual = atual.proximo

        anterior.proximo = None

    def size(self):
        atual = self.head
        c = 0

        while atual is not None:
            atual = atual.proximo
            c += 1

        return c
    
    def remove(self):
        atual = self.head
        self.head = atual.proximo
        self.qtd -= 1

    def __len__(self): #Questão 5
        return self.qtd

    def remove_item(self, item): #Questão 6
        atual = self.head
        anterior = None
        self.qtd -= 1
        
        while atual is not None:
            if atual.dados == item:
                break
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == None: 
            raise Exception("Item não está na lista")
        
        if anterior == None:
            self.head = atual.proximo
        else:
            anterior.proximo = atual.proximo 
        
    def show(self): #Questão 7
        lista = []
        atual = self.head

        while atual is not None:
            lista.append(atual.dados)
            atual = atual.proximo

        return lista

    def reverse(self): #Questão 10
        listaEncadeada = []
        atual = self.head

        while atual is not None:
            listaEncadeada.append(atual.dados)
            atual = atual.proximo

        l1 = []
        while len(listaEncadeada) > 0:
            l1.append(listaEncadeada.pop())

        return l1
    
    def clear(self): #Questão 13
        atual = self.head

        while atual is not None:
            atual = atual.proximo
            self.remove()

    def concat(self, lista): #Questão 15
        atual = self.head

        while atual.proximo is not None:
            atual = atual.proximo
            
        atual.proximo = lista.head
        self.qtd += len(lista)

    def __str__(self):
        atual = self.head
        result = '['
        
        while atual != None:
            result += str(atual.getData())
            if  atual.getNext(): result += ", "
            atual = atual.getNext()
        result += ']'
        return result

#12, 14, 16, 17, 18, 19, 20, 21

if __name__ == '__main__':
    lE = ListaEncadeada()
    lE2 = ListaEncadeada()

    lE.append(1)
    lE.append(2)
    lE.append(4)
    lE.append(5)

    lE.insert(2, 3)
    lE.pop()
    lE.remove_item(1)
    #lE.clear()

    print(lE.show())

    lE2.append(2)
    lE2.append(4)
    lE2.append(8)
    lE2.append(10)
    
    lE.concat(lE2)

    print(f"Quantidade de itens com Size: {lE.size()}")
    print(f"Quantidade de itens com Len: {len(lE)}")
    print(f"Lista invertida: {lE.reverse()} \n")

    print(lE.show())