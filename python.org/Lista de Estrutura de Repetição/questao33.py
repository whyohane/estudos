'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as 
um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas. '''

num = int(input("Digite quantas temperaturas deseja registrar: \n"))

temp = float(input("Digite a temperatura:\n"))

soma = temp
maiorTemp = temp
menorTemp = temp

for i in range (num - 1):

    temp = float(input("Digite a temperatura: \n"))
    soma = soma + temp

    if temp > maiorTemp :
        maiorTemp = temp

    if temp < menorTemp :
        menorTemp = temp

media = soma/num
print("A maior temperatura registrada foi {} graus, a menor foi {} graus e a média das temperaturas é {} graus.\n".format(maiorTemp, menorTemp, media))