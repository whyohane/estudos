'''Crie um programa que realiza a PA de 20 elementos com primeiro termo e razao pelo usuario.'''

primeiroT = int(input("Digite o primeiro termo da PA: \n"))
razao = int(input("Digite a razão da PA: \n"))

PA = primeiroT + (20-1) * razao

for i in range (primeiroT, PA, razao):
    print(i)
