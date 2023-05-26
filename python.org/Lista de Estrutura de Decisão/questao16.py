'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''

print("Programa para calcular equação do segundo grau.\n")
a = float(input("Digite o valor de A: \n"))
if a == 0 :
    print("NÃO É POSSIVEL CALCULAR ESSA EQUAÇÃO! \n")
else:
    b = float(input("Digite o valor de B: \n"))
    c = float(input("Digite o valor de C: \n"))

    delta = b**2 -4*a*c
    if delta < 0 :
        print("Não existem raízes reais!!! \n")
    elif delta == 0 :
        y1 = (-b + (delta**1/2))/2*a
        print("Possui apenas uma raiz real: {}".format(y1))
    else : 
        y1 = (-b + (delta**1/2))/2*a
        y2 = (-b - (delta**1/2))/2*a
        print("Possui duas raízes reais: {} e {}".format(y1, y2))

