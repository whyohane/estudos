'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou
para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. '''

num = int(input("Verificador de números primos! Digite um número inteiro para delimitar o intervalo: \n"))

aux = 0
divs = 0
divisores = []
i = 1

while i <= num :
    while aux <= i :
        aux = 0
        aux += 1
        if i % aux == 0 :
            divisores.append(aux)
            divs += 1
            aux += 1
            
        if divs <= 2 :
            print("O número {} é primo e seus divisores são: {}.\n".format(i, divisores))
        else :
            print("O número {} não é primo e seu divisores são: {}.\n".format(i, divisores))
    i += 1