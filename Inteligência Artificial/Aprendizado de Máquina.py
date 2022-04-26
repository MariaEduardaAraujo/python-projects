from sklearn import tree

X = [[-1, -1], [0, 0], [1, 1], [2, 2]]
y = [0, 0, 1, 1]

modelo = tree.DecisionTreeClassifier()
modelo.fit(X, y)

resultado = modelo.predict([[5, 5]])

print(resultado)


#==================================================#

from sklearn import svm

X = [[-1, -1], [0, 0], [1, 1], [2, 2]]
y = [0, 0, 1, 1]

modelo = svm.SVC()
modelo.fit(X, y)

resultado = modelo.predict([[-5, -5]])

print(resultado)
