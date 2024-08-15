import random

def forca(tentativas):
    estados = [
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        ----------
        """,
        """
         -----
         |   |
         O   |
             |
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
             |
        ----------
        """    
    ]
    
    print(estados[tentativas])


print("Seja bem-vind@ ao...")
print("Jogo da Forca dos Países nas Olimpíadas!")
print("="*30)

paises = ["Estados Unidos","China","Japão","Austrália","França","Países Baixos",
"Grã-Bretanha","Coreia do Sul","Alemanha","Itália","Nova Zelândia","Canadá",
"Uzbequistão","Hungria","Espanha","Suécia","Quênia","Noruega","Irlanda","Brasil"]

random.shuffle(paises)
paisSecreto = (paises[0]).upper()

print("Você terá 6 chances de acertar o país secreto")
print("E atingirá a forca caso perca todas as suas chances!")
print("="*30)
print()

opcao = str(input("Você deseja participar? [S/N] ")).upper()
print()

try:
    if (opcao == "S" or opcao == "SIM"):
        chances = 6
        while (chances != 0):
            for i in range(len(paisSecreto)):
                print("_", end=" ")
            
            print()
            chutePalavra = str(input("Digite uma palavra: ")).upper()
            chutePalavra.strip()

            if (chutePalavra == paisSecreto):
                    print("Parabens! Você acertou!!!")
                    break
            else:
                if (chutePalavra != paisSecreto):
                    print("Que pena, essa não é a palavra secreta! Tente novamente!")
                    print(f"Você tem: {chances - 1}")
                    print()
                    chances-=1
                    forca(chances)
        if(chances == 0):
            print("Que pena, você perdeu!")
            print(f"A palavra era: {paisSecreto}")
    else:
        print("Até a próxima!")

except Exception as e:
    print(f"O erro {e} ocorreu")