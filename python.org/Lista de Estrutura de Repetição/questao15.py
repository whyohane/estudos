'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo. '''

print("Série de Fibonacci.\n")

n = int(input("Digite um número inteiro qualquer para delimitar a série de Fibonacci.\n"))

cont = 1
a1 = 1
a2 = 1
fibo = 0
print(fibo)
fibo = a1
print(fibo)
fibo = a2
print(fibo)

while cont < (n-2) :
    fibo = a1 + a2
    a1 = fibo
    a2 = fibo - a2
    print(fibo)
    cont +=1