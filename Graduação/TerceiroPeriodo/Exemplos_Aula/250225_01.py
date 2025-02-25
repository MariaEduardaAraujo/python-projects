'''#1. Inverter Strings
def inverter(p):
    if (len(p) == 0):
        return ""
    else:
        return p[-1] + inverter(p[:-1])

assert inverter("abc") == "cba"
assert inverter("Python") == "nohtyP"
assert inverter("banana") == "ananab"
assert inverter("recussão") == "oãssucer"
assert inverter("ChatGPT") == "TPGtahC"'''


'''#2. Número Perfeito
def eh_perfeito(a, i = 1):
    if (a == i):
        return 0
    if (a % i == 0):
        return i + eh_perfeito(a, i+1)
    else:
        return eh_perfeito(a, i+1)

def verifica(a):
    return eh_perfeito(a) == a

def soma_perfeitos(a, b):
    if (a > b):
        return 0
    if (verifica(a)):
        return a + soma_perfeitos(a+1, b)
    return soma_perfeitos(a+1, b)

assert soma_perfeitos(20, 28) == 28
assert soma_perfeitos(6, 14) == 6
assert soma_perfeitos(6, 28) == 34'''