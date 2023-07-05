'''Faça um programa para imprimir: para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. '''

def enesimo_num(num):

    for aux in range (1, num + 1):

        cont = 1

        while cont <= aux:

            print(cont, end=' ')
            cont += 1
            
        print()    

num = int(input("Digite um número inteiro: \n"))
enesimo_num(num)
    
        
