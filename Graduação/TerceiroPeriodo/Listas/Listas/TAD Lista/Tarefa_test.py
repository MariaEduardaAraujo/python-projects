#Aula 11/03/2025

from Tarefa import *
from ListaTarefa import *

#Questão 1
'''t1 = Tarefa("Fazer compras", "Média")
print(t1)'''

lista = ListaTarefas()

def teste_adicionar_no_fim():
    t1 = Tarefa("Ler um livro", "Baixa")
    lista.adicionar_no_fim(t1)
    t2 = Tarefa("T2", "Média")
    lista.adicionar_no_fim(t2)
    t3 = Tarefa("T3", "Alta")
    lista.adicionar_no_fim(t3)
    t7 = Tarefa("T7", "Baixa")
    lista.adicionar_no_fim(t7)
    t8 = Tarefa("T8", "Média")
    lista.adicionar_no_fim(t8)
    t9 = Tarefa("T9", "Alta")
    lista.adicionar_no_fim(t9)
    t10 = Tarefa("T10", "Baixa")
    lista.adicionar_no_fim(t10)

def teste_adicionar_em_posicao():
    print("\nAdicionar no fim e em posição")
    t4 = Tarefa("T4", "Baixa")
    lista.adicionar_em_posicao(t4, 0)
    t5 = Tarefa("T5", "Média")
    lista.adicionar_em_posicao(t5, 3)
    t6 = Tarefa("T6", "Alta")
    lista.adicionar_em_posicao(t6, 9) 
    t11 = Tarefa("T11", "Alta")
    lista.adicionar_em_posicao(t11, -1) #Posição Inválida

teste_adicionar_no_fim()
teste_adicionar_em_posicao()

'''print(lista.tarefas[0])
print(lista.tarefas[1])
print(lista.tarefas[2])
print(lista.tarefas[3])
print(lista.tarefas[4])
print(lista.tarefas[5])
print(lista.tarefas[6])
print(lista.tarefas[7])
print(lista.tarefas[8])
print(lista.tarefas[9])'''

def teste_obter_tarefa():
    print("\nObter_tarefa")
    print(lista.obter_tarefa(0))
    print(lista.obter_tarefa(5))
    print(lista.obter_tarefa(8))
    print(lista.obter_tarefa(-1)) #Posição Inválida

def teste_remover_tarefa():
    print("\nRemover_tarefa")
    lista.remover_tarefa(0)
    lista.remover_tarefa(5)
    lista.remover_tarefa(9)

def teste_contem():
    print("\nContem")
    t1 = Tarefa("Ler um livro", "Baixa")
    print(lista.contem(t1))

teste_obter_tarefa()
teste_remover_tarefa()
teste_contem()

def teste_tamanho():
    print("\nTamanho")
    lista2 = ListaTarefas()
    print(lista2.tamanho)

    t12 = Tarefa("T12", "Baixa")
    lista2.adicionar_no_fim(t12)
    print(lista2.tamanho)

    t13 = Tarefa("T13", "Média")
    t14 = Tarefa("T14", "Alta")
    t15 = Tarefa("T15", "Baixa")
    lista2.adicionar_no_fim(t13)
    lista2.adicionar_no_fim(t14)
    lista2.adicionar_no_fim(t15)
    print(lista2.tamanho)

teste_tamanho()

'''print()
print(f"P1: {lista.tarefas[0]}")
print(f"P2: {lista.tarefas[1]}")
print(f"P3: {lista.tarefas[2]}")
print(f"P4: {lista.tarefas[3]}")
print(f"P5: {lista.tarefas[4]}")
print(f"P6: {lista.tarefas[5]}")
print(f"P7: {lista.tarefas[6]}")
print(f"P8: {lista.tarefas[7]}")
print(f"P9: {lista.tarefas[8]}")
print(f"P10: {lista.tarefas[9]}")'''