'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. '''

vetor1 = []
vetor2 = []
vetor3 = []
resultado = []

elementos = 10

for i in range (elementos):

    num = int(input("Digite um valor para preencher o primeiro vetor: \n"))
    vetor1.append(num)

for i in range (elementos):

    num = int(input("Digite um valor para preencher o segundo vetor: \n"))
    vetor2.append(num)

for i in range (elementos):

    num = int(input("Digite um valor para preencher o terceiro vetor: \n"))
    vetor3.append(num)

for i in range (elementos):
    resultado.append(vetor1[i])
    resultado.append(vetor2[i])
    resultado.append(vetor3[i])


print("O resultado intercalado com as listas é:\n {}".format(resultado))
