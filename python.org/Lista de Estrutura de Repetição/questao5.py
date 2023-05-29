'''Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. '''

anos = 0

popu_A = float(input("Digite o número de habitantes do país A: \n"))
taxa_A = float(input("Digite a porcentagem de crescimento do país A: \n"))
popu_B = float(input("Digite o número de habitantes do país B: \n"))
taxa_B = float(input("Digite a porcentagem de crescimento do país B: \n"))

taxa_A = taxa_A/100
taxa_B = taxa_B/100

while popu_A < popu_B :
    crescPopu_A = popu_A * taxa_A
    popu_A = int(popu_A + crescPopu_A)

    crescPopu_B = popu_B * taxa_B
    popu_B = int(popu_B + crescPopu_B)

    anos += 1

print("Com {} anos o país A irá ultrapassar com {} habitantes a população do país B com {} habitantes.\n".format(anos, popu_A, popu_B))
