'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. '''

def soma_numeros(n1, n2, n3):

    soma = n1+n2+n3
    return soma

num1 = int(input("Digite um número: \n"))
num2 = int(input("Digite um número: \n"))
num3 = int(input("Digite um número: \n"))

soma = soma_numeros(num1, num2, num3)
print("A soma dos números é:", soma)