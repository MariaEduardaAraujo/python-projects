'''Lista de Exercícios 02 (Revisão - Strings)
Instruções:
Desenvolva seu algoritmo para os problemas abaixo.
Crie suas próprias funções, não utilize funções preexistentes da linguagem.'''

'''1. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar é palíndroma.
Escreva um programa que verifique se uma palavra dada é palíndroma.
https://www.thehuxley.com/problem/1008?locale=pt_BR'''

'''2. Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de palavras de um
texto. Escreva um programa que determine o número de palavras de um texto dado.
https://www.thehuxley.com/problem/1008?locale=pt_BR - Contar palavras'''

'''3. Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. Exemplo: Se a string digitada
for "José da Silva", deverá ser impresso na tela a substring "Silva".
https://www.thehuxley.com/problem/248?locale=pt_BR - Última palavra de uma frase'''

'''4. As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria indicado por Andrade/Carlos. Escreva um
programa que lê um nome e o escreve no formato acima.'''

'''5. As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de um livro texto, etc., exigem que o
nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um
programa que receba um nome e o escreva no formato de bibliografia.'''

'''6. É muito comum que os títulos de documentos como avisos, declarações, atestados, etc., apareçam em letras maiúsculas
separadas por um espaço em branco. Escreva uma função que receba uma palavra e a retorne no formato acima.

def separa(palavra):
    for letra in palavra:
        print(letra.capitalize(), end=" ")

texto = input("Digite uma palavra para ser separada por espaços: ")
separa(texto)'''

'''7. Escreva uma função que gere logins para usuários de um sistema de computação baseado na seguinte regra: o login é
composto pelas letras iniciais do nome do usuário.'''

'''8. Os editores de texto possuem um recurso que permite o usuário substituir uma palavra de um texto por outra palavra.
Escreva um programa que realize esta ação numa frase dada.'''