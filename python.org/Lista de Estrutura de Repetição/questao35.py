'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma 
lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. '''

num = int(input("Verificador de números primos! Digite um número inteiro para delimitar o intervalo: \n"))

for my_number in range (1, num + 1):
    divisores = []
    divs = 0
    for divisor in range (1, my_number + 1) :

        if my_number % divisor == 0 :
            divisores.append(divisor)
            divs += 1
    
    if divs <= 2 :
        print("O número {} é primo e tem {} divisores, sendo eles: {}\n".format(my_number, divs, divisores))
    else :
        print("O número {} não é primo e tem {} divisores, sendo eles: {}\n".format(my_number, divs, divisores))