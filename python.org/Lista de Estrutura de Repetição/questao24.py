'''Faça um programa que calcule o mostre a média aritmética de N notas. '''

print("Programa para calcular a média de notas!\n")

num = int(input("Digite quantos números deseja calcular: \n"))
soma = 0

for i in range (num) :
    notas = float(input("Digite a nota: \n"))
    soma = soma + notas

media = soma/num
print("O valor da média das notas é : {}.\n".format(media))

