data = open("Base De Gastos.txt", "a")
data.write("Gastos:\n ")
data.close()

#open and read the file after the appending:
data = open("Base De Gastos.txt", "r")
print(data.read())
