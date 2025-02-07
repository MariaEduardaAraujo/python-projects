'''Lista de Exercícios 02 (Revisão - Strings)
Instruções:
Desenvolva seu algoritmo para os problemas abaixo.
Crie suas próprias funções, não utilize funções preexistentes da linguagem.'''

'''#1. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar é palíndroma.
Escreva um programa que verifique se uma palavra dada é palíndroma.
https://www.thehuxley.com/problem/1008?locale=pt_BR

def verificar_palindromo(palavra):
    palavraInvertida = palavra[::-1]
    
    if (palavra == palavraInvertida):
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

palavra = input("Digite uma palavra: ")
verificar_palindromo(palavra)

#2. Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de palavras de um
texto. Escreva um programa que determine o número de palavras de um texto dado.
https://www.thehuxley.com/problem/1008?locale=pt_BR - Contar palavras

texto = input("Digite um texto aqui: ")
separa = texto.split(" ")
palavras = 0

for p in separa:
    palavras += 1

print(f"O seu texto tem {palavras} palavras")

#3. Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. Exemplo: Se a string digitada
for "José da Silva", deverá ser impresso na tela a substring "Silva".
https://www.thehuxley.com/problem/248?locale=pt_BR - Última palavra de uma frase

nomeCompleto = input("Digite seu nome completo: ")

separaNome = nomeCompleto.split(" ")
ultimoSobrenome = separaNome[-1]

print(ultimoSobrenome)

#4. As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria indicado por Andrade/Carlos. Escreva um
programa que lê um nome e o escreve no formato acima.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

separaNome = nome.split(" ")
separaSobrenome = sobrenome.split(" ")

primeiroNome = separaNome[0]
ultimoSobrenome = separaSobrenome[-1]

print(ultimoSobrenome+"/"+primeiroNome)

#5. As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de um livro texto, etc., exigem que o
nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um
programa que receba um nome e o escreva no formato de bibliografia.

def login(nome, sobrenome):
    separaNome = (nome.upper()).split(" ")
    separaSobrenome = (sobrenome.title()).split(" ")
    primNome = ''
    sobrenome = ''

    for nome in separaNome:
        primNome += nome[0] + ". "
    for sobrenome in separaSobrenome:        
        sobrenome = separaSobrenome[-1]
    
    print(f"Seu nome em formato bibliográfico é: {sobrenome +", "+ primNome}")

nomeUsuario = input("Digite seu nome: ")
sobrenomeUsuario = input("Digite seu sobrenome: ")
login(nomeUsuario, sobrenomeUsuario)

#6. É muito comum que os títulos de documentos como avisos, declarações, atestados, etc., apareçam em letras maiúsculas
separadas por um espaço em branco. Escreva uma função que receba uma palavra e a retorne no formato acima.

def separa(palavra):
    for letra in palavra:
        print(letra.capitalize(), end=" ")

texto = input("Digite uma palavra para ser separada por espaços: ")
separa(texto)

#7. Escreva uma função que gere logins para usuários de um sistema de computação baseado na seguinte regra: o login é
composto pelas letras iniciais do nome do usuário.

def login(nomeUsuario):
    separa = (nomeUsuario.lower()).split(" ")
    userName = ''

    for nome in separa:
        userName += nome[0]
    print(f"Seu login é: {userName}")

nomeUsuario = input("Digite seu nome: ")
login(nomeUsuario)'''

'''8. Os editores de texto possuem um recurso que permite o usuário substituir uma palavra de um texto por outra palavra.
Escreva um programa que realize esta ação numa frase dada.'''

