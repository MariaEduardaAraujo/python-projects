#Aula 11/03/2025

from Tarefa import *

class ListaTarefas:
    def __init__(self):
        self.capacidade = 10
        self.tamanho = 0
        self.tarefas = [None] * self.capacidade

    def adicionar_no_fim(self, tarefa):
        if (self.tamanho == self.capacidade): return "Lista cheia"
        self.tarefas[self.tamanho] = tarefa
        self.tamanho += 1
        
    def adicionar_em_posicao(self, tarefa, posicao):
        if (self.tamanho == self.capacidade or posicao < 0 or posicao > self.tamanho): return " "
        
        for i in range(self.tamanho, posicao, -1):  
            self.tarefas[i] = self.tarefas[i - 1]

        self.tarefas[posicao] = tarefa
        self.tamanho += 1
    
    def obter_tarefa(self, posicao):
        if (posicao > self.tamanho or posicao < 0): return "Posição Inválida!"
        return self.tarefas[posicao]

    def remover_tarefa(self, posicao):
        if (posicao < 0 or posicao > self.tamanho): return "Posição Inválida!"
        
        for i in range(posicao, self.tamanho-1):
            self.tarefas[i] = self.tarefas[i+1]
        
        self.tarefas[self.tamanho - 1] = None  
        self.tamanho -= 1
        print("Tarefa removida!")

    def contem(self, tarefa):
        for t in range(self.tamanho):
            if self.tarefas[t].descricao == tarefa.descricao: return True
        return False
    
    def tamanho(self):
        return self.tamanho