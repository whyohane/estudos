'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de 
cada aluno, imprima o número de alunos com média maior ou igual a 7.0. '''

print("Programa de notas e médias!\n")

numAlunos = 0
medias = []

for alunos in range(1, 11):
    somaNotas = 0
    for notas in range(1, 5):
        
        nota = float(input("Digite a {} nota do aluno {}.\n".format(notas, alunos)))
        somaNotas += nota

    media = somaNotas/4
    medias.append(media)

    if media >= 7:
        
        numAlunos += 1

print("A média dos alunos foram: {} e apenas {} alunos tiveram média acima de 7.\n".format(medias, numAlunos))