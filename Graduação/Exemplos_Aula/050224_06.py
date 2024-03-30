'''Solicite a idade de 5 alunos, e apresente a media das idades. Sabendo que, para cada 
pergunta, mostre da seguinte maneira: Exemplo: Aluno X, qual a sua idade? 
Substituindo o X pela posição do aluno que está perguntando.'''

somaIdades = 0;

for i in range(1, 6):
  idade = int(input(f"Aluno {i}, qual a sua idade? "));
  somaIdades = somaIdades + idade;

print(f"Média das idades = {somaIdades/5}");