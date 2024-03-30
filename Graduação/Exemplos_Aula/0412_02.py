'''
Data da aula: 04/12/2023
Professor: Kenji
Curso: BSI
'''

nome = input("Digite o seu nome: ");
print(f"Seja\nbem\nvindo\n{nome}");

#convertendo a entrada do input para int
av1 = int(input("Digite a 1a nota: "));
av2 = int(input("Digite a 2a nota: "));
media = (av1+av2)/2;

#f vem de f-string
print(f"Media = {media}");