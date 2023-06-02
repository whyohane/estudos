'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela. '''

notas = []
soma = 0

for i in range(1, 5):
    nota = float(input("Digite a nota {}:\n".format(i)))
    notas.append(nota)
    soma += nota

media = soma/4
print("As notas são: {} e a média é: {}\n".format(notas, media))