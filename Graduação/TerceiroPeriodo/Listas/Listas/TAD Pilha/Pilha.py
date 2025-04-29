from is_full import *

class Pilha:
    def __init__(self, MAXIMO=10):
        self.capacidade = MAXIMO
        self.pilha = []

    def __str__(self):
        return f"{self.pilha}"
    
    def adicionar(self, e):
        if len(self.pilha) == self.capacidade: raise is_full("Pilha Cheia!")
        self.pilha.append(e)
    
    '''def is_full(self):
        if len(self.pilha) == self.capacidade: print("Pilha Cheia!")'''
    
    def remover(self):
        if len(self.pilha) > 0:
            self.pilha.pop()
    
    def topo(self):
        if len(self.pilha) > 0:
            return self.pilha[-1]
        pass

    def remover_recurs(self):
        if len(self.pilha) == 0: 
            print("Lista Vazia!")
            return
        self.pilha.pop()
        self.remover_recurs()

    def inverter(self):
        lista = []
        pilha = self.pilha[:] #Cópia de self.pilha
        if len(pilha) > 0:
            for e in range(len(pilha), 0, -1):
                lista.append(e)
                pilha.pop()

            return lista
        
        '''#inverte
            def inverte(self):
                lista = [1,2,3,4]
                for i in range(len(lista),0,-1):
                    self.pilha.append(i)
                    lista.pop()

                    for d in range (len(self.pilha)):
                        lista.append(self.pilha.pop())
                    print(lista)'''

    def copia(self):
        q = []
        if len(self.pilha) > 0:
            for e in self.pilha:
                q.append(e)
            print("Pilha q:", q)

    def menor(self):
        men = 99
        if len(self.pilha) > 0:
            for e in self.pilha:
                if e < men:
                    men = e
            return men