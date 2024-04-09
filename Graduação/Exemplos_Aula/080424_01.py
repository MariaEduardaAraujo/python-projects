import funcao_externa as validacao

validacao.validar_cpf(123)
validacao.validar_nome("Maria")
validacao.validar_convidados("A", 19)
validacao.numero_com_parametro

# Sobreposição não funciona 
'''
validacao.validar_numero()
validacao.validar_numero(5)'''