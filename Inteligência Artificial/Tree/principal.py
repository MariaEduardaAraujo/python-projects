from numpy.core.fromnumeric import size
from sklearn import tree
import csv

X = [[]] # inclui uma linha
X.pop(0) # remove a primeira linha

# PASSO 1: Carregar os atributos (ou features) do dataset de treinamento para treinar
# o classificador sem a coluna target a coluna ID
with open("treinamento.csv") as arquivo:
    linhas = csv.reader(arquivo)
    next(linhas)
    for linha in linhas:
        linha.pop()
        linha.pop(0)
        X.append(linha)
        
# PASSO 2: Carregar a variavel "target" do dataset de treinamento para trreinar o classificador
y = []
with open("treinamento.csv") as arquivo:
    linhas = csv.reader(arquivo)
    next(linhas)
    for linha in linhas:
        target = linha.pop(16)
        y.append(target)
        
# PASSO 3: Treinar o classificador com os dados de treino
clf = tree.DecisionTreeClassifier() # arvore ou svm
clf = clf.fit(X, y)


# PASSO 4: Utilizar os dados de teste para realizar a predição
T = [[]]
T.pop(0)
with open("teste.csv") as arquivo:
    linhas = csv.reader(arquivo)
    next(linhas)
    for linha in linhas:
        linha.pop(0)
        T.append(linha)


# PASSO 5: Realizar a predição
listaResultados = clf.predict(T)
print(listaResultados)

# PASSO 6 : Criar uma lista com os ID do teste para montar o resultado final
listaIDsTeste = [[]]
listaIDsTeste.pop(0)
with open("teste.csv") as arquivo:
    linhas = csv.reader(arquivo)
    next(linhas)
    for linha in linhas:
        listaIDsTeste.append(linha.pop(0))

# PASSO 7: Criar um arquivo com os id de teste e os resultados da predição
novoArquivoResultados = open("resultado.csv", 'w', newline='')
escritor = csv.writer(novoArquivoResultados)
for i in range(len(listaResultados)):
    escritor.writerow([listaIDsTeste[i], listaResultados[i]])
novoArquivoResultados.close()
