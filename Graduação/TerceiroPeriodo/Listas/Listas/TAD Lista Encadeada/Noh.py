class Noh:
    def __init__(self, valor):
        self.dados = valor
        self.proximo = None
    def getData(self):
        return self.dados
    def getNext(self):
        return self.proximo
    def setData(self, novoValor):
        self.dados = novoValor
    def setNext(self, novoProximo):
        self.proximo = novoProximo
    def __str__(self):
        return f"Noh: {str(self.getData())} | Próximo: {str(self.getNext())}"