'''Faça um programa para imprimir: para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. '''

def enesima_linha(num): 
    for aux in range (1, num + 1):
        cont = 1

        while True:
            print(aux, end=' ')
            
            if cont == aux:
                break
            cont+= 1
        print ()

num = int(input("Digite um número inteiro: \n"))
enesima_linha(num)
    
