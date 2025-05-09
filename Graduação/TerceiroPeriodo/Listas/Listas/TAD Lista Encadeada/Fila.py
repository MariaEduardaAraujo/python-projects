from Noh import *

class Fila: #Questão 8
    def __init__(self):
        self.head = None

    def append(self, item):
        novo = Noh(item)

        if self.head == None:
            self.head = novo
            return
        
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo

    def remove(self):
        atual = self.head
        self.head = atual.proximo

    def __str__(self):
        lista = []
        atual = self.head

        while atual.proximo is not None:
            lista.append(atual.dados)
        
        return lista

if __name__ == '__main__':
    f = Fila()

    f.append(1)
    f.append(2)
    f.append(4)
    f.append(5)

    f.remove()

    print(f)