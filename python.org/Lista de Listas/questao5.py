'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. '''

print("\nPrograma verificador de pares e impares! \n")

numeros = []
par = []
impar = []

for i in range(20):

    num = int(input("Digite um número inteiro: \n"))
    numeros.append(num)

    if num % 2 == 0 :
        par.append(num)
    else :
        impar.append(num)

print("Os números lidos foram: {}\n".format(numeros))
print("Os números pares são: {}\n".format(par))
print("Os números impares são: {}\n".format(impar))