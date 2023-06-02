'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo
vetor. Imprima a idade e a altura na ordem inversa a ordem lida. '''

idades = []
alturas = []

for pessoas in range (0, 5):

    idade = int(input("Digite a idade da pessoa {}:\n".format(pessoas + 1)))
    altura = int(input("Digite a altura em centimetros:\n"))

    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print("As idades reversas: {}\n".format(idades))
print("As alturas reversas são: {}\n".format(alturas))