'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares. '''

print("Programa verificador de números ímpares e pares!\n")
par = 0
impar = 0

for cont in range (10) :
    num = int(input("Digite um número qualquer: \n"))
    if num % 2 == 0 :
        print("\n{} é um número par.\n".format(num))
        par += 1
    else :
        print("\n{} é um número ímpar.\n".format(num))
        impar += 1

print("Existem {} números pares e {} números ímpares. \n".format(par, impar))


