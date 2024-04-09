#Strings
nomeDaInstituicao = "IFAL"
print(type(nomeDaInstituicao))

frase1 = "Ele disse que está falando 'a verdade'"
frase2 = '"Ser ou não ser, eis a questão"'
print(frase1)
print(frase2)

#Concatenação
uf = "AL"
print(nomeDaInstituicao, uf)

#Funções da String
print("Tamanho da String: ", len(nomeDaInstituicao)) #Retorna tamanho da String
print("Posição da letra 'A' na String: ", nomeDaInstituicao.find("A")) #Retorna a posição da 
#primeira ocorrência na String (Exibe "-1" se não encontrar)
print("Posição da letra 'L' na String, a partir da posição 1: ", nomeDaInstituicao.find("L", 1))
#Procura a partir de uma determinada posição
print("Posição da letra 'L' na String, a partir da posição 1 com fim na posição 3: ", nomeDaInstituicao.find("L", 1, 4))
#Procura a partir de uma determinada posição com começo e fim
print("Muda para a primeira letra maiúscula: ", nomeDaInstituicao.capitalize())
#Muda apenas o primeiro caractere da palavra para maiusculo, o resto fica minusculo 
print("'IFAL' para 'IFAL Maceió': ",nomeDaInstituicao.replace("IFAL", "IFAL Maceió"))
#Muda a String para uma nova String
print("Upper e Lower: ", nomeDaInstituicao.upper(), nomeDaInstituicao.lower())
#Muda para maiúsculo (upper) e minúsculo (lower)
print("Número de ocorrências da letra 'A': ", nomeDaInstituicao.count("A")) #Conta o número de ocorrências de uma determinada substring na String.