'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''

print("Programa para dias da semana.\n")

num = int(input("Digite um número de 1 a 7.\n"))

if num == 1 :
    print("{} é domingo.".format(num))
elif num == 2 :
    print("{} é segunda.\n".format(num))
elif num == 3 :
    print("{} é terça.\n".format(num))
elif num == 4 :
    print("{} é quarta.\n".format(num))
elif num == 5 :
    print("{} é quinta. \n".format(num))
elif num == 6 :
    print("{} é sexta. \n".format(num))
elif num == 7 :
    print("{} é sábado. \n".format(num))