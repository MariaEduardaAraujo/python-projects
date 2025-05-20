class HashTable:
    def __init__(self):
        self.tamanho = 4
        self.slots = [None] * self.tamanho
        self.valores = [None] * self.tamanho
        self.qtd = 0

    def hash(self, chave, tamanho):
        return chave%tamanho
    
    def rehash(self, oldhash, tamanho):
        return (oldhash+1)%tamanho

    def put(self, chave, valor):
        valor_hash = self.hash(chave, len(self.slots))
        self.qtd += 1
        fatorCarga = self.qtd/self.tamanho

        if fatorCarga <= 0.8:
            if self.slots[valor_hash] == None:
                self.slots[valor_hash] = chave
                self.valores[valor_hash] = valor
            else:
                if self.slots[valor_hash] == chave:
                    self.valores[valor_hash] = valor
                else:
                    proximo = self.rehash(valor_hash, len(self.slots))

                    while self.slots[proximo] != None and self.slots[proximo] != chave:
                        proximo = self.rehash(proximo, len(self.slots))

                    if self.slots[proximo] == None:
                        self.slots[proximo] = chave
                        self.valores[proximo] = valor
                    else:
                        self.valores[proximo] = valor
        else:
            self.new_put()
            self.put(chave, valor)
    
    def get(self, chave):
        slot_inicial = self.hash(chave, len(self.slots))
        valor = None
        posicao = slot_inicial

        while True:
            if self.slots[posicao] == chave:
                valor = self.valores[posicao]
                return valor
            else:
                posicao = self.rehash(posicao, len(self.slots))
                if posicao == slot_inicial:
                    break

    def __getitem__(self, chave):
        return self.get(chave)
    
    def __setitem__(self, chave, valor):
        self.put(chave, valor)

    def __str__(self):
        return f"Chave: {self.slots} | Valor: {self.valores}"

    def __len__(self): #Questão 1
        return self.qtd
    
    def __contains__(self, chave): #Questão 2
        slot_inicial = self.hash(chave, len(self.slots))

        while self.slots[slot_inicial] != None:
            if self.slots[slot_inicial] == chave:
                return True
            else:
                posicao = self.rehash(slot_inicial, len(self.slots))
                slot_inicial = posicao
    
    def new_put(self): #Questão 12
        novTam = (2 * self.tamanho)
        novSlots = self.slots
        novVal = self.valores
        
        self.slots = [None]*novTam
        self.valores = [None]*novTam
        self.tamanho = novTam
        self.qtd = 0 

        for i in range(len(novSlots)):
            if novSlots[i] is not None:
                self.put(novSlots[i], novVal[i])

if __name__ == '__main__':
    hs = HashTable()

    print("Adicionando: ")
    hs.put(13, "A")
    hs.put(33, "B")
    hs.put(11, "C")
    hs.put(8, "D")
    hs.put(2, "E")

    print(f"\nTestando Get: {hs.get(13)}")
    print(f"Quantidade: {len(hs)}")
    print(f"Está na lista: {hs.__contains__(33)} \n")
    print(hs)