# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo. 

int1 = int(input("Digite o primeiro número inteiro: \n"))
int2 = int(input("Digite o segundo número inteiro: \n"))
numReal = float(input("Digite um número real: \n"))

produto = (int1 * 2) * (int2 / 2)
soma = (int1 * 3) + numReal
elevado = numReal**3

print("O produto do dobro do primeiro com metade do segundo: \n", produto)
print("A soma do triplo do primeiro com o terceiro: \n", soma)
print("O terceiro elevado ao cubo: \n", elevado)
