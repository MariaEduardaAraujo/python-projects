class Deque:
    def __init__(self):
        self.capacidade = 5
        self._dados = [None]*self.capacidade
        self._tamanho = 0
        self._inicio = 0
    
    def __str__(self):
        return self._dados

    def __len__(self):
        return self._tamanho
    
    def is_empty(self):
        return self._tamanho == 0
    
    def first(self):
        if self.is_empty(): raise Exception('A Fila está vazia')
        return self._dados[self.inicio]
    
    def last(self):
        if self.is_empty(): raise Exception('A Fila está vazia')
        #Indice do último item
        return (self._inicio + self._tamanho - 1) % len(self._dados)
    
    def add_last(self, e): #Igual as Filas
        if self._tamanho == len(self._dados): self._aumenta_tamanho(2 * len(self._dados))
        
        p = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[p] = e
        self._tamanho += 1

    def add_first(self, e):
        if self._tamanho == len(self._dados): self._aumenta_tamanho(2 * len(self._dados))

        else: 
            lista = self._dados[:]

            for i in range(self._tamanho):
                self._dados[self._inicio] = None
                self._dados[i+1] = lista[i]
            self._dados[self._inicio] = e

            t = 0
            for i in self._dados:
                if i != None:
                    t += 1
            self._tamanho = t


    def remove_first(self): #Igual as Filas
        if self.is_empty(): raise Exception('A Fila está vazia')
        
        r = self._dados[self._inicio]
        self._dados[self._inicio] = None
        
        nI = (self._inicio + 1) %len(self._dados)
        self._inicio = nI
        self._tamanho -= 1
        
        return r
    
    def remove_last(self):
        if self.is_empty(): raise Exception('A Fila está vazia')
        
        r = self._dados[self.last()]
        self._dados[self.last()] = None
        self._tamanho -= 1

        return r
    
    def _aumenta_tamanho(self, novo_tamanho):
        dados_antigos = self._dados 
        self._dados = [None] * novo_tamanho 
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao] 
            posicao = (1 + posicao) %len(dados_antigos)
        self._inicio = 0


if __name__ == '__main__':
    d = Deque()

    d.add_last(1)
    d.add_last(2)
    d.add_last(3)
    d.add_first(4)
    d.add_first(5)
    
    d.remove_first()
    #d.remove_first()
    d.remove_last()
    #d.remove_last()

    print(d._dados)