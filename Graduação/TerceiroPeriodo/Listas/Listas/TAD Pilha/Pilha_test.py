from Pilha import*

p = Pilha()
p2 = Pilha(2)

def test_adicionar():
    print("\nAdicionar")
    p.adicionar(1)
    p.adicionar(2)
    p.adicionar(3)
    p.adicionar(4)
    p.adicionar(5)
    p.adicionar(6)

def test_remover():
    print("\nRemover")
    p.remover()

def test_topo():
    print("\nVer Topo")
    print(p.topo())

'''def test_remover_recurs():
    print("\nRemover Recursivamente")
    p.remover_recurs()'''

def test_inverter():
    print("\nInverter Pilha")
    print(p.inverter())

def test_copia():
    print("\nCopia Pilha")
    p.copia()

def test_menor():
    print("\nMenor Valor")
    print(p.menor())

test_adicionar()
test_remover()
test_topo()
#test_remover_recurs()
test_inverter()
test_copia()
test_menor()

print(p)