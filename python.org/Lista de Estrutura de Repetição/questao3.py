'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''

nome = input("digite seu nome: \n")

while len(nome) <= 3 :
    nome = input("digite um nome maior que 3 caracteres: \n")
else:
    print("nome validado!")

idade = int(input("digite sua idade:\n"))

while idade < 0 or idade > 150 :
    idade = int(input("idade inválida! digite sua idade corretamente: \n"))
else :
    print("idade validada!")

salario = float(input("digite seu salário: \n"))

while salario < 0 :
    salario = float(input("digite um salário maior que zero!\n"))
else :
    print("salário validado!")

gen = input("digite 'f' para feminino ou 'm' para masculino.\n")

while gen != "f" and gen != "m" :
    gen = input("digite um genero válido!\n")
else :
    print("genero validado.\n")

estadoC = input("digite um estado civil: s, c, v, d.\n")

while estadoC != "s" and estadoC != "c" and estadoC != "v" and estadoC != "d" :
    estadoC = input("digite um estado civil válido! \n")
else :
    print("genero validado!\n")
