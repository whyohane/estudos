'''Entre com um número e verifique se ele é primo, caso não seja, retorne quantas vezes esse número é divisivel: '''

num = int(input("Digite um valor qualquer: \n"))

if num == 0 and num == 1 : 
    print("Não é possivel calcular esse número. \n")
else : 
    divs = 0

    for i in range(1, num+1) :
        if num % i == 0 :
            divs += 1
if divs == 2:
    print("É um número primo.\n")
else:
    print("Não é um número primo e possui {} divisores. \n".format(divs))

