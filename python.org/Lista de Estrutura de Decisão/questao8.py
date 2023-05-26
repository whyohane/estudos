'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
 sabendo que a decisão é sempre pelo mais barato. '''

print("Programa para calcular o produto mais barato.\n")
num1 = float(input("Digite um valor: \n"))
num2 = float(input("Digite o segundo valor: \n"))
num3 = float(input("Digite o terceiro valor: \n"))

menor = num1

if menor < num2 and menor < num3 :
    print("O menor valor é {}. \n".format(num1))

menor = num2

if menor < num1 and menor < num3 :
    print("O menor valor é {}. \n".format(num2))

menor = num3

if menor < num1 and menor < num2 :
    print("O menor valor é {}. \n".format(num3))