'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total. '''

print("Programa para calcular quantos litros de tinta precisa para pintar parede. \n")

metros = float(input("Digite quantos metros quadrados de parede deseja pintar: \n"))

litros = metros / 3

latas = (litros // 18) + 1

valorTotal = latas * 80

print("Você precisa de {} latas para pintar {} metros, pagando um total de: {} reais.".format(latas, metros, valorTotal))