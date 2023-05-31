'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1. '''

num = int(input("Verificador de números primos! Digite um número inteiro: \n"))

if num <= 0 :
    print("O número não pode ser verificado.\n")
else :
    aux = 1
    divs = 0

    while aux <= num :
        if num % aux == 0 :
            divs += 1
        aux += 1
        
    if divs <= 2 :
        print("O número {} é primo.\n".format(num))
    else :
        print("O número {} não é primo.\n".format(num))
