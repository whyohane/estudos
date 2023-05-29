'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento. '''

popu_A = 80000
taxa_A = 3/100

popu_B = 200000
taxa_B = 1.5/100

anos = 0

print("O país A tem : {} habitantes.\n".format(popu_A))
print("O país B tem {} habitantes.\n".format(popu_B))

while popu_A < popu_B :
    crescPopu_A = popu_A * taxa_A
    popu_A = int(popu_A + crescPopu_A)

    crescPopu_B = popu_B * taxa_B
    popu_B = int(popu_B + crescPopu_B)

    anos += 1

print("Com {} anos o país A agora possui {} habitantes e o país B possui {} habitantes.\n".format(anos, popu_A, popu_B))
