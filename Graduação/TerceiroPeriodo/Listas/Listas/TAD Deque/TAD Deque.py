# Questão 5 e 10
class TAD_Deque:
    def __init__(self):
        self.capacidade = 10
        self.deque = [None]*self.capacidade
        
        self.inicio = 0
        self.tamanho = 0

        self.fila = []

    def __str__(self):
        return f"{self.deque}"
    
    def add_first(self, e):
        if self.capacidade == self.tamanho: pass

        elif self.tamanho == 0: self.add_last(e)

        else:
            lista = self.deque[:]

            for x in range(self.tamanho):
                self.deque[self.inicio] = e
                self.deque[x+1] = lista[x]

            t = 0

            for i in self.deque:
                if i != None:
                    t += 1
            self.tamanho = t
        
    def add_last(self, e):
        if self.capacidade == self.tamanho: pass

        p = (self.inicio + self.tamanho) %len(self.deque)
        self.deque[p] = e  
        self.tamanho += 1

    def delete_first(self):
        if self.tamanho == 0: pass

        r = self.deque[self.inicio]
        self.deque[self.inicio] = None

        nI = (self.inicio + 1) %len(self.deque)
        self.inicio = nI
        self.tamanho -= 1

        return r

    def delete_last(self):
        if self.tamanho == 0: pass

        indice = (self.inicio + self.tamanho - 1) % len(self.deque)
        r = self.deque[indice]
        self.deque[indice] = None
        self.tamanho -= 1

        return r
    
    def first(self):
        return self.deque[self.inicio]
    
    def last(self):
        indice = (self.inicio + self.tamanho - 1) % len(self.deque)
        return self.deque[indice]
    
    def add_fila(self, e):
        self.fila.append(e)

    def soma(self): # Questão 7
        s = 0
        for e in self.deque:
            if e != None:
                s += int(e)
        return s
    
    def add_middle(self, e, posicao): # Questão 11
        lista = self.deque[:]

        for i in range(self.tamanho):
            if i == posicao:
                self.deque[i] = e
                for j in range(i, self.tamanho):
                    self.deque[j+1] = lista[j]
                break

if __name__ == '__main__':
    #Questão 1
    '''d = TADdeque()

    d.add_first(4)
    d.add_last(8)
    d.add_last(9)
    d.add_first(5)

    print(d.last())
    d.delete_first()
    d.delete_last()
    d.add_last(7)

    print(d.first())
    print(d.last())
    d.add_last(6)
    d.delete_first()

    d.delete_first()
    print(d.deque)'''

    #Questão 2 e 7
    d = TAD_Deque()

    d.add_last(1)
    d.add_last(2)
    d.add_last(3)
    d.add_last(4)
    d.add_last(5)
    d.add_last(6)
    d.add_last(7)
    d.add_middle(8, 2) # Questão 11

    '''for i in range(d.tamanho):
        d.add_fila(d.delete_first())

    print(d.deque)
    print(d.fila)'''

    print(d.deque)
    print(d.soma())
    