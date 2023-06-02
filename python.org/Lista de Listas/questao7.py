'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números. '''

numeros = []
soma = 0
multiplicacao = 1

for i in range (5):
    num = int(input("Digite um número inteiro: \n"))
    soma += num
    multiplicacao *= num
    numeros.append(num)

print("Os números lidos foram: {}, a soma deles é {} e a multiplicação é {}.\n".format(numeros, soma, multiplicacao))
