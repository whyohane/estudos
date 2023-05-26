'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; '''

print("Programa verificador de triângulos. \n")
l1 = float(input("Digite o primeiro lado: \n"))
l2 = float(input("Digite o segundo lado: \n"))
l3 = float(input("Digite o terceiro lado: \n"))

# "se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo."

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2 :
    if l1 == l2 == l3 :
        print("É um triângulo equilátero.\n")
    elif l1 == l2 or l2 == l3 or l3 == l1 :
        print("É um triângulo isósceles.\n")
    elif l1 != l2 != l3 :
        print("É um triângulo escaleno.\n")
else:
    print("Não é um triângulo.\n")