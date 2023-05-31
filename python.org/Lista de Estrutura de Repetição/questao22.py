'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível. '''

num = int(input("Verificador de números primos! Digite um número inteiro: \n"))

if num <= 0 :
    print("O número não pode ser verificado.\n")
else :
    aux = 1
    divs = 0
    divisores = []
    while aux <= num :
        if num % aux == 0 :
            divisores.append(aux)
            divs += 1
            

        aux += 1
        
    if divs <= 2 :
        print("O número {} é primo e seus divisores são: {}.\n".format(num, divisores))
    else :
        print("O número {} não é primo e seu divisores são: {}.\n".format(num, divisores))