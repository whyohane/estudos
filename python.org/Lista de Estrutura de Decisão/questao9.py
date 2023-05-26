'''Faça um Programa que leia três números e mostre-os em ordem decrescente. '''

print("Programa para ler 3 números e mostrar em ordem decrescente.\n")

num1 = float(input("Digite um número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

menor = num1

if menor < num2 and menor < num3 :
    print("O menor valor é {}. \n".format(num1))
    menorNum = menor

menor = num2

if menor < num1 and menor < num3 :
    print("O menor valor é {}. \n".format(num2))
    menorNum = menor

menor = num3

if menor < num1 and menor < num2 :
    print("O menor valor é {}. \n".format(num3))
    menorNum = menor

maior = num1

if maior > num2 and maior > num3 :
    print("O maior valor é {}. \n".format(num1))
    maiorNum = maior

maior = num2

if maior > num1 and maior > num3 :
    print("O maior valor é {}. \n".format(num2))
    maiorNum = maior

maior = num3

if maior > num1 and maior > num2 :
    print("O maior valor é {}. \n".format(num3))
    maiorNum = maior

meio = num1

if meio < maiorNum and meio > menorNum :
    print("O valor do meio é {}.\n".format(meio))

meio = num2

if meio < maiorNum and meio > menorNum :
    print("O valor do meio é {}.\n".format(meio))

meio = num3

if meio < maiorNum and meio > menorNum :
    print("O valor do meio é {}.\n".format(meio))