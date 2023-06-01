'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma
é jovem, adulta ou idosa, conforme a média calculada. '''

print("Programa para calcular a média de idades!\n")

num = int(input("Digite o número de pessoas que deseja entrar a idade: \n"))
soma = 0

for i in range (num) :
    idade = int(input("Digite a idade de uma pessoa: \n"))
    soma = soma + idade

media = soma/num

if media >= 0 and media <= 25 :
    print("A média de idades é {}, então a turma de {} pessoas é considerada jovem.\n".format(media, num))
elif media >= 26 and media <= 60 :
    print("A média de idades é {}, então a turma de {} pessoas é considerada adulta.\n".format(media, num))
else :
    print("A média de idades é {}, então a turma de {} pessoas é considerada idosa.\n".format(media, num))