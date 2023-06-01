'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou
para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. '''

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

