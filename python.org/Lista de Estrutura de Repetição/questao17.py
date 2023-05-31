'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120 '''

num = int(input("Digite um número qualquer para ser calculado o seu fatorial: \n"))

fat = num
aux = num - 1
        
while aux > 1 : 
    fat = fat * aux
    aux = aux - 1

print("Fatorial de {} é {}".format(num, fat))
