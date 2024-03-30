print(""" 1-Cadastrar veiculos 
          2-Exibir todos veiculos
          3-Exibir o total de veiculos cadastrados
          4-Exibir todos veiculos em ordem alfabetica
          5-Localizar Carro
          6-Remover carro
          7-Verificar se existem duplicados
          8-Exibir nome e a posicao dos duplicados
          9-Exibir quantas letras tem o nome do carro
          10-Exibir quantidade vogais no nome do carro
          11-Sair  """)

opcao = int(input("Selecione a opção: "))
veiculos = []

def cadastrarVeiculos():
  carro = input("Informe o nome do carro: ")
  veiculos.append(carro)

def exibirVeiculos():
  print(veiculos)

def obterTotalDeveiculos():
  return len(veiculos)

def organizarLista():
  veiculos.sort()

def exibirEmOrdemAlfabetica():
  organizarLista()
  print(veiculos)

def localizarPosicaoCarro():
      carro = input("Informe o carro a ser localizado: ")
      posicao = veiculos.index(carro)
      print("O carro",carro," foi encontrado na posição: ",posicao)

def removerCarro() :
  carro = input("Informe o veículo a ser removido: ")
  veiculos.remove(carro)
  print("Veículo removido")
  
def existemDuplicados() :
    nomecarro= input("Informe o nome do veículo: ")
    cont=0
    for carrodalista in veiculos :
       if nomecarro == carrodalista :
          cont = cont+1
       if cont>1:
          print("Existe duplicado")

def exibirPosicaoDuplicados():
  nomecarro= input("Informe o nome do veículo: ")
  print(" O veículo aparece na posição: ",veiculos.index(nomecarro))

def exibirQuantasletras():
  carro = input("Informe o carro a ser contado: ")
  print(len(carro))
  
def exibirQuantasVogais():
  numerodevogais =input("Qual o veículo? ")
  cont=0
  for i in numerodevogais:
      if i=='a':
        cont=cont+1
      if i=='e':
        cont=cont+1
      if i=='i':
        cont=cont+1
      if i=='o':
        cont=cont+1
      if i=='u':
        cont=cont+1 
  print(cont)

while opcao != 11 :
  if opcao == 1 :
    cadastrarVeiculos()
  elif opcao == 2 :
      exibirVeiculos()
  elif opcao == 3 :
    print("Total de carros",obterTotalDeveiculos())
  elif opcao == 4 :
      exibirEmOrdemAlfabetica()
  elif opcao == 5 :
     localizarPosicaoCarro()
  elif opcao == 6 :
      removerCarro();
  elif opcao == 7 :
     existemDuplicados()
  elif  opcao==8:
    exibirPosicaoDuplicados()
  elif opcao==9:
    exibirQuantasletras()
  elif opcao==10:    
    exibirQuantasVogais()  
  opcao = int(input("Selecione a opção: "))
