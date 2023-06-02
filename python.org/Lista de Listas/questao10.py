'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. '''

vetor1 = []
vetor2 = []
vetor3 = []

elementos = 10

for i in range (elementos):

    num = int(input("Digite um valor para preencher o primeiro vetor: \n"))
    vetor1.append(num)

for i in range (elementos):

    num = int(input("Digite um valor para preencher o segundo vetor: \n"))
    vetor2.append(num)

for i in range (elementos):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("O vetor 3 intercalado com ambas as listas é:\n {}".format(vetor3))
