'''Crie uma lista de 1 a 5, faça um loop e some os pares ex: 1+1, 2+2, 3+3...'''

lista = [1, 2, 3, 4, 5]

for x in lista :
    a = x + x
    soma = soma + a
    print("A soma de pares é: \n", a)
    print("A soma de todos os pares é: \n", soma)
        