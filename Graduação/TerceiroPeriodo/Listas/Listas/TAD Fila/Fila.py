class Fila:
    def __init__(self, c):
        self.capacidade = c
        self.fila = [None]*self.capacidade
        self.tamanho = 0
        self.inicio = 0
    
    def __str__(self):
        return self.fila
    
    def enqueue(self, e):
        if self.tamanho == self.capacidade: raise Exception ("Fila Cheia!")
        p = (self.inicio + self.tamanho) %len(self.fila) #Fim da fila
        self.fila[p] = e
        self.tamanho += 1

    def dequeue(self):
        if self.tamanho == 0: raise Exception ("Fila Vazia!")

        r = self.fila[self.inicio]
        self.fila[self.inicio] = None

        nI = (self.inicio + 1) %len(self.fila) #Novo início
        self.tamanho -= 1
        self.inicio = nI

        return r

    def rodar(self):
        if self.tamanho == 0: raise Exception ("Fila Vazia!")
        
        self.enqueue(self.dequeue())

if __name__ == '__main__':
    fila = Fila(5)

    fila.enqueue(5)
    fila.enqueue(3)
    fila.dequeue()
    fila.enqueue(2)
    fila.enqueue(8)
    fila.dequeue()

    fila.enqueue(9)
    fila.enqueue(1)
    fila.dequeue()
    fila.enqueue(7)
    fila.enqueue(6)
    fila.dequeue()

    fila.dequeue()
    fila.enqueue(4)
    fila.dequeue()
    fila.dequeue()

    fila.rodar()

    print(fila.fila)