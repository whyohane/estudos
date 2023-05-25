'''Crie um programa que realiza a contagem de 1 até 100, usando apenas números impares , ao final do processo
exiba em tela quantos números impares foram encontrados nesse intervalo, assim como a soma dos mesmos.'''

print("Programa para números impares. \n")

print("Esses são os números impares de 1 até 100: \n")

impares = 1
cont = 0
soma = 0

while impares < 100 :
    print(impares)
    cont += 1
    soma = soma + impares
    impares = impares + 2

print("Foram encontrados {} números impares no intervalo. \n".format(cont))
print("A soma desses números é: ", soma)



