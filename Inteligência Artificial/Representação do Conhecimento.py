from experta import *

class Anamnese(Fact):
    pass

class Diagnostico(KnowledgeEngine):
    @Rule(Anamnese(febre='nao'))
    def saudavel(self):
        print("Você não está com febre.")
    @Rule(Anamnese(febre='sim'))
    def doente(self):
        print("Você está com febre. Procure um médico, pois você pode estar doente.")

diagnostico = Diagnostico()
diagnostico.reset()

resp = input("Você está com febre? ")

diagnostico.declare(Anamnese(febre = resp))

diagnostico.run()
