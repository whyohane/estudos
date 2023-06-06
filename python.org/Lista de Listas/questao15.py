'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem'''

valores = []
cont = 0
soma = 0

while True:
    notas = float(input("Digite um valor aleatório: \n"))

    if notas == -1:
        break
    else:
        valores.append(notas)
        cont += 1
        soma += notas

print("Foram lidos {} valores!\n".format(cont))

print("A lista dos valores lidos: {}\n".format(valores))

valores.reverse()

for i in range(len(valores)):
    print("\n", valores[i])

print("A soma dos valores é: {}.\n".format(soma))

media = soma/cont

print("A média dos valores lidos é: {}\n".format(media))

valores.reverse()

for i in range(len(valores)) :

    if valores[i] > media :
        print("O valor {} está acima da média calculada.\n".format(valores[i]))

    if valores[i] < 7 :
        print("O valor {} é menor do que 7.\n".format(valores[i]))

print("OBRIGADA PELA PARTICIPAÇÃO!\n")