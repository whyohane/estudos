'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. '''

lista = []

for i in range (10):

    num = int(input("Digite um número inteiro: \n"))
    lista.append(num)

lista.reverse()
print("A lista de números na ordem inversa é: {}\n".format(lista))