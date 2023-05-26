'''Faça um Programa que verifique se uma letra digitada é 
"F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''

print("Programa identificador de gênero. \n")

gen = input("Digite 'F' para sexo feminino e 'M' para másculino. \n")

if gen == 'F' :
    print("Você é do sexo feminino. \n")
elif gen == 'M' :
    print("Você é do sexo masculino. \n")
else :
    print("Sexo inválido. \n")