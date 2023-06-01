'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos. '''

print("Programa para calcular a média de alunos por turma.\n")

num = int(input("Digite o número de turmas:\n"))
soma = 0

for i in range(1, num + 1) :
    alunos = int(input("Digite a quantidade de alunos da turma {}:\n".format(i)))

    while alunos > 40 :
        alunos = int(input("Turmas não podem ter 40 alunos. Digite o valor correto:\n"))

    soma = soma + alunos

media = soma/num
print("A média de alunos por {} turmas é: {}\n".format(num, media))
    
    
    


