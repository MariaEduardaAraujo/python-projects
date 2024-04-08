from sklearn  import tree
import graphviz

atributos = [ [-1,-1], [-2,-2],[-3,-3], [0,0],[1,1], [2,2]] # matriz com os atributos
rotulo = [0, 0, 0, 0, 1, 1] # rotulo com o rotulo

classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(atributos, rotulo)

#=============================================================================#
#grafico = tree.export_graphviz(classificador) #cria um arquivo com a árvore que foi criada pelo classificador a partir dos dados

#graph = graphviz.Source(grafico)

#png_bytes = graph.pipe(format="png")

#with open("arvore.png", "wb") as f:
#    f.write(png_bytes)

#=============================================================================#
op = 'n'

while(op.upper() != 'S'):
    at0 = input("Informe o atributo 0: ")  
    at1 = input("Informe o atributo 1: ")  

    at_novo = [[at0,at1]]

    resultado = classificador.predict(at_novo)

    print(resultado)

    op = input("Sair? (S/N) ")

