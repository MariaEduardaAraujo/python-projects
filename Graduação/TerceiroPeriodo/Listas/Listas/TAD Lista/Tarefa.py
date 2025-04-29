#Aula 11/03/2025

#Questão 1
class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade
    def __str__(self):
        return f"Tarefa: {self.descricao} (Prioridade: {self.prioridade})"
