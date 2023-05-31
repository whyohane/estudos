'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. '''

print("Programa para ler os números ímpares entre 1 e 50. \n")

i = 1

while i < 50 :
    if i % 2 == 1 :
        print ("O número {} é ímpar.\n".format(i))

    i += 1