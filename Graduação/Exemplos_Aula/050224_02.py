'''#Quando o número for divisível por 3, escreve Fizz.
   #Quando for divisível por 5, escreve Buzz.
   #Quando for divisível por 3 e por 5, escreve FizzBuzz
   #Quando não for divisível por 3 e por 5, escreve o próprio número

for i in range (1, 101,):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print(i)
'''

'''
for i in range (1, 11, 2):
    print(f"O número {i} é ímpar")

for i in range (0, 11, 2):
    print(f"O número {i} é par")
    
for i in range (10, 0, -1):
    print(i)
'''