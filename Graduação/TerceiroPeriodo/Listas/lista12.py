from lista11 import BinaryTree

def divideNum(fpexp): # Questão 2
    numero, num2 = "", ""
    for c in fpexp:
        if c not in ["(","+", "-", "*", "/", ")"]:
            num2 += c
        else:
            if num2:
                numero += num2 + " "
                num2 = ""
            numero += c + " "
    if num2:
        numero += num2
    return numero.split()

def buildParseTree(fpexp):
    fplist = divideNum(fpexp)
    pStack = []
    eTree = BinaryTree('')
    
    pStack.append(eTree)
    currentTree = eTree
    
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    import operator
    opers = {'+':operator.add, '-':operator.sub,'*':operator.mul, '/':operator.truediv}
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
def preorder(self):
    print(self.key)
    if self.leftChild:
        preorder(self.leftChild)
    if self.rightChild:
       preorder(self.rightChild)

def postorder(self):
    if self != None:
        postorder(self.getLeftChild())
        postorder(self.getRightChild())
        print(self.getRootVal())

def inorder(self):
    if self != None:
        inorder(self.getLeftChild())
        print(self.getRootVal())
        inorder(self.getRightChild())

def altura(self): # Questão 6
    altEsq, altDir = 0, 0

    if self.leftChild:
        altEsq = altura(self.leftChild)
    if self.rightChild:
        altDir = altura(self.rightChild)

    if altDir > altEsq:
        return altDir + 1
    return altEsq + 1

def conta_nos(self): # Questão 7
    c = 0
    fila = []
    fila.append(self)

    while len(fila):
        noh = fila.pop(0)
        c += 1

        if noh.leftChild:
            fila.append(noh.leftChild)
        if noh.rightChild:
            fila.append(noh.rightChild)
    return c

def conta_folhas(self):
    c = 0

    if self.lefChild is not None and self.rightChild is not None:
        pass

if __name__ == "__main__":
    pt = buildParseTree("((10+5)*3)"); 
    print(pt)
    print(evaluate(pt))

    print(f"Preorder: ")
    preorder(pt)
    print(f"Postorder: ")
    postorder(pt)
    print(f"Inorder: ")
    inorder(pt)

    print(f"Altura: {altura(pt)}")
    print(f"Quantidade de nós: {conta_nos(pt)}")
