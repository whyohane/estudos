'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500. '''

print("Série de Fibonacci.\n")

cont = 1
a1 = 1
a2 = 1
fibo = 0
print(fibo)
fibo = a1
print(fibo)
fibo = a2
print(fibo)

while fibo < 500 :
    fibo = a1 + a2
    a1 = fibo
    a2 = fibo - a2
    cont +=1
    if fibo < 500 :
        print(fibo)
    