class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def __repr__(self):
        l = self.leftChild
        r = self.rightChild
        return (f'[ {self.key}, [{l}], [{r}] ] ')

    def eh_folha(self): 
        return self.leftChild is None and self.rightChild is None
    
    def tem_filho(self):
        return self.leftChild is not None or self.rightChild is not None

    def altura(self):
        altEsq, altDir = 0, 0

        if self.leftChild:
            altEsq = self.leftChild.altura()
        
        if self.rightChild:
            altDir = self.rightChild.altura()

        if altDir > altEsq:
            return altDir + 1
        return altEsq + 1
    
    def conta_nos(self):
        c = 0
        fila = []
        fila.append(self)

        while len(fila):
            no = fila.pop(0)
            c += 1

            if no.leftChild:
                fila.append(no.leftChild)
            if no.rightChild:
                fila.append(no.rightChild)
        return c

if __name__ == '__main__':
    bt = BinaryTree("a") # Questão 6

    bt.insertLeft("b")
    bt.insertLeft("c")
    bt.insertRight("d")
    bt.insertLeft("e")
    bt.setRootVal("g")
    bt.insertLeft("h")

    print(bt)
    print(bt.eh_folha()) # Questão 9
    print(bt.tem_filho()) # Questão 10
    print(bt.altura()) # Questão 11
    print(bt.conta_nos()) # Questão 12

    #====================================
    print()
    bt2 = BinaryTree("a") # Questão 8
 
    bt2.insertLeft("b")
    e = bt2.getLeftChild()
    e.insertLeft("c")
    d = e.getLeftChild()
    d.insertRight("d")

    e = bt2.getLeftChild()
    e.insertRight("e")
    d = e.getRightChild()
    d.insertLeft("f")

    bt2.insertRight("g")
    e = bt2.getRightChild()
    e.insertLeft("h")
    d = e.getLeftChild()
    d.insertLeft("i")

    print(bt2)
    print(bt2.eh_folha()) # Questão 9
    print(bt2.tem_filho()) # Questão 10
    print(bt2.altura()) # Questão 11
    print(bt2.conta_nos()) # Questão 12