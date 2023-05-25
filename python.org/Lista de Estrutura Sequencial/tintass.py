'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    1- comprar apenas latas de 18 litros;
    2- comprar apenas galões de 3,6 litros;
    3- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''

metros = float(input("Digite quantos metros quadrados precisa pintar: \n"))

litros = metros / 6

# Primeiro caso: Apenas latas de 18 litros.
latasGrandes = (litros // 18) + 1

valorTotal = latasGrandes * 80

print("Você pode comprar {} latas grandes para pintar {} metros, pagando um total de: {} reais. \n".format(latasGrandes, metros, valorTotal))

# Segundo caso: Apenas latas de 3,6 litros.
latasPequenas = (litros // 3.6) + 1

valorTotal = latasPequenas * 25

print("Você pode comprar {} latas pequenas para pintar {} metros, pagando um total de: {} reais. \n".format(latasPequenas, metros, valorTotal))

# Terceiro caso: Misturar ambas as latas.
if litros < 18:
    latasPequenas = (litros// 3.6) + 1
    valorTotal = latasPequenas * 25
    print ("Você pode comprar apenas {} latas pequenas, pagando {} reais. \n".format(latasPequenas, valorTotal))
else:
    latasGrandes = 0
    latasPequenas = 0

    while litros >= 18 :
        latasGrandes += 1
        litros = litros - 18
    
    while litros > 0 :
        latasPequenas += 1
        
        if litros < 3.6 :
            latasPequenas += 1
            litros = 0
        else :  
            litros = litros - 3.6

    valorTotal = (latasGrandes * 80) + (latasPequenas * 25)
    print("Você pode comprar {} latas grandes e {} latas pequenas, pagando no total {} reais. \n".format(latasGrandes, latasPequenas, valorTotal))