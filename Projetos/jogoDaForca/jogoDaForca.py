import random
import string

def forca(tentativas):
    estados = [
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
             |
             |
        ----------
        """,
        """
         -----
         |   |
             |
             |
             |
        ----------
        """    
    ]
    
    print(estados[tentativas])

def letras():
    palavra = " ".join(paisSecreto)
    letraAdv = " "
    for l in alfabeto:
        for letra in palavra:
            if (l == letra):
                if (letra in chutePalavra):
                    letraAdv += letra
    print("As seguintes letras estão na palavra: ", " ".join(letraAdv))
    print()
            

print("Seja bem-vind@ ao...")
print("Jogo da Forca dos Países nas Olimpíadas!")
print("="*30)

paises = ["Estados Unidos","China","Japão","Austrália","França","Países Baixos",
"Grã-Bretanha","Coreia do Sul","Alemanha","Itália","Nova Zelândia","Canadá",
"Uzbequistão","Hungria","Espanha","Suécia","Quênia","Noruega","Irlanda","Brasil"]

random.shuffle(paises)
paisSecreto = (paises[0]).upper()
alfabeto = list(string.ascii_uppercase)

print("Você terá 6 chances de acertar o país secreto")
print("E atingirá a forca caso perca todas as suas chances!")
print("="*30)
print()

opcao = str(input("Você deseja participar? [S/N] ")).upper()
print()

try:
    if (opcao == "S" or opcao == "SIM"):
        nivel = int(input("Selecione o nível de dificuldade: [1/2/3] "))
        if (nivel == 1):
            chances = 6
            print(f"Você tem {chances} chances para tentar acertar a palavra")
            print()
        elif (nivel == 2):
            chances = 4
            print(f"Você tem {chances} chances para tentar acertar a palavra")
            print()
        else:
            chances = 3
            print(f"Você tem {chances} chances para tentar acertar a palavra")
            print()

        while (chances != 0):
            for i in range(len(paisSecreto)):
                print("_", end=" ")
            
            print()
            chutePalavra = str(input("Digite uma palavra: ")).upper()
            chutePalavra.strip()

            if (chutePalavra == paisSecreto):
                    print("Parabéns! Você acertou!!!")
                    break
            else:
                if (chutePalavra != paisSecreto):
                    print("Que pena, essa não é a palavra secreta! Tente novamente!")
                    print(f"Você tem: {chances - 1} chances")
                    print()

                    chances-=1
                    forca(chances)
                    letras()

        if(chances == 0):
            print("Que pena, você perdeu!")
            print(f"A palavra era: {paisSecreto}")
    else:
        print("Até a próxima!")

except Exception as e:
    print(f"O erro {e} ocorreu")