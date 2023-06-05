'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos 
com mais de 13 anos possuem altura inferior à média de altura desses alunos. '''

idades = []
alturas = []

idade = 0
altura = 0
alunos = 30
soma = 0
alunosBaixos = 0

for i in range(alunos) :

    idade = int(input("Digite a idade do aluno {}:\n".format(i)))
    altura = int(input("Digite a altura do aluno {} em centimetros:\n".format(i)))

    idades.append(idade)
    alturas.append(altura)

    soma += altura

media = soma/alunos

print("A média das alturas dos alunos é: {}.".format(media))

for i in range(len(idades)) :

    if idades[i] > 13 :

        if alturas[i] < media :

            alunosBaixos += 1
            print("O aluno {} com idade {} tem altura {} centimetros, sendo então, inferior a média.\n".format(i, idades[i], alturas[i]))

