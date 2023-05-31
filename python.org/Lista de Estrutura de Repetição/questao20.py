'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.'''

cond = 1

while cond == 1 :
    num = int(input("Digite um número qualquer para ser calculado o seu fatorial: \n"))
    if num > 0 or num < 16 :
        fat = num
        aux = num - 1
        
        while aux > 1 : 
            fat = fat * aux
            aux = aux - 1

        print("Fatorial de {} é {}".format(num, fat))
        cond = int(input("Digite 1 para calcular o fatorial de um número ou outro número para sair.\n"))
    else :
        num = int(input("Digite um número válido! \n"))