'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, 
ele será classificado como "Inocente".'''

print("QUESTIONÁRIO CRIMINAL!\n")

print("Para responder as perguntas, digite 'sim' ou 'não'.\n")

cont = 0

pergunta1 = input("Já telefonou para a vítima?\n")

if pergunta1 == 'sim':
    cont += 1

pergunta2 = input("Esteve no local do crime?\n")

if pergunta2 == 'sim':
    cont += 1

pergunta3 = input("Mora perto da vítima?\n")

if pergunta3 == 'sim':
    cont += 1

pergunta4 = input("Devia para a vitima?\n")

if pergunta4 == 'sim':
    cont += 1

pergunta5 = input("Já trabalhou com a vítima?\n")

if pergunta5 == 'sim':
    cont +=1

if cont == 2:
    print("É UMA PESSOA SUSPEITA!\n")
elif cont == 3 or cont == 4:
    print("É UM CÚMPLICE!\n")
elif cont == 5:
    print("É O ASSASSINO!\n")
else:
    print("É INOCENTE!\n")
