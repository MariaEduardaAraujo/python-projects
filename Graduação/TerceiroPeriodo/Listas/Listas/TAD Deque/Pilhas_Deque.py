# Questão 4
class Pilhas_Deque:
    def __init__(self):
        self.pilha1, self.pilha2 = [], []
        self.inicio = 0
        self.tamanho = 0

    def __str__(self):
        return f"{self.pilha1, self.pilha2}"
    
    def push(self, e):
        self.pilha1.append(e)
        self.tamanho += 1

    def pop(self):
        if len(self.pilha1) > 0:
            self.pilha1.pop()
            self.tamanho -= 1
        else:
            self.pilha2.pop()
            self.tamanho -= 1

    def pop_top(self):
        for _ in range(len(self.pilha1)):
            self.pilha2.append(self.pilha1.pop())

        self.pilha2.pop()
        self.tamanho -= 1

    def top(self):
        if len(self.pilha1) > 0:
            indice = len(self.pilha1)
            return self.pilha1[indice-1]
        else:
            indice = len(self.pilha2)
            return self.pilha2[indice-1]
        

    def add_last(self, e): #O(1)
        self.push(e)

    def remove_first(self): #O(1)
        self.pop_top()
    
    def remove_last(self): #O(1)
        self.pop()

    def last(self): #O(1)
        return self.top()

if __name__ == '__main__':
    d = Pilhas_Deque()

    d.add_last(1)
    d.add_last(2)
    d.add_last(3)
    d.add_last(4)
    d.add_last(5)
    d.add_last(6)

    d.remove_last()
    d.remove_last()
    d.remove_first()

    print(d.last())
    print(f"{d.pilha1}, {d.pilha2}")