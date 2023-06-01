'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. '''

print("Programa contador de votos!")

num = int(input("Digite quantas pessoas irão votar: \n"))

cand1 = 0
cand2 = 0
cand3 = 0

for i in range(num) :
    voto = int(input("Eleitor, digite o seu voto entre 1 e 3.\n"))
    if voto == 1:
        cand1 += 1
    elif voto == 2 :
        cand2 += 1
    elif voto == 3 :
        cand3 += 1
    else :
        print("Voto invalidado!\n")

print("{} pessoas votaram no candidato 1.\n".format(cand1))
print("{} pessoas votaram no candidato 2.\n".format(cand2))
print("{} pessoas votaram no candidato 3.\n".format(cand3))

