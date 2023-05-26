'''Faça um Programa que leia três números e mostre o maior e o menor deles. '''

print("Programa para ler o maior e o menor número entre 3 inputs.\n")
num1 = float(input("Digite um número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

maior = num1

if maior > num2 and maior > num3 :
    print("O maior número é o número {}. \n".format(num1))

maior = num2

if maior > num1 and maior > num3 :
    print("O maior número é o número {}. \n".format(num2))

maior = num3

if maior > num1 and maior > num2 :
    print("O maior número é {}. \n".format(num3))

menor = num1

if menor < num2 and menor < num3 :
    print("O menor número é o número {}. \n".format(num1))

menor = num2

if menor < num1 and menor < num3 :
    print("O menor número é o número {}. \n".format(num2))

menor = num3

if menor < num1 and menor < num2 :
    print("O menor número é {}. \n".format(num3))