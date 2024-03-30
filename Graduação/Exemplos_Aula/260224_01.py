import random;

numeroSecreto = random.randint(1, 10);
chutes = [];

for i in range(1, 4):
    chute = int(input("Digite o seu chute? "));
    chuteDado = False;
    
    for j in range(0, len(chutes)):
        if(chute == chutes[j]):
            print("Chute já foi dado!");
            chuteDado = True;

    if(chuteDado == False):
        chutes.append(chute);

    if(chute == numeroSecreto):
        print("Acertou!")
        break;
    elif (chute != numeroSecreto):
            if (chute > numeroSecreto):
                print("O número secreto é menor")
            else:
                print("O número secreto é maior")
                
print("Chutes dados:")
for x in range(0, len(chutes)):
    print(chutes[x], end=" ")