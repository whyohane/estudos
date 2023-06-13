'''# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list.
*Hint* you may want to make or find a helper function that determines if a given number is prime or not.'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
primes = []
for num in numbers:
    if num <= 0 :
        print("O número {} não pode ser verificado.\n".format(num))
    else :
        aux = 1
        divs = 0
        divisores = []
        while aux <= num :
            if num % aux == 0 :
                divisores.append(aux)
                divs += 1
                
            aux += 1
            
        if divs <= 2 :
            print("O número {} é primo e seus divisores são: {}.\n".format(num, divisores))
            primes.append(num)
        else :
            print("O número {} não é primo e seu divisores são: {}.\n".format(num, divisores))

print('A lista de números primos é:')
print(primes)