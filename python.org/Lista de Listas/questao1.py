'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. '''

lista = []

for i in range(5) :
    num = int(input("Digite um número inteiro.\n"))
    lista.append(num)

print("A lista de 5 números é:{}".format(lista)) 