'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um. '''

num = int(input("Digite quantos CDs deseja calcular: \n"))
soma = 0

for i in range (num) :
    preço = float(input("Digite o valor pago no CD: \n"))
    soma = soma + preço

media = soma/num
print("O valor médio pago em cada CD é :{}.\n".format(media))