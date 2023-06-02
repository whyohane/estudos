'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e 
determine se ele é ou não um número primo.'''

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