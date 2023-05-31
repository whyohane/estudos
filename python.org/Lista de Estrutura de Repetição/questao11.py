'''Altere o programa anterior para mostrar no final a soma dos números. '''

num1 = int(input("Digite um número qualquer: \n"))
num2 = int(input("Digite outro número qualquer: \n"))
soma = 0

for x in range(num1, num2) :
    soma = soma + x

print("A soma de números do intervalo entre os números {} e {} é {}.\n".format(num1, num2, soma))