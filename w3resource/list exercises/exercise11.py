''' # Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
odd_numbers = []

for i in numbers:

    if i % 2 != 0:

        odd_numbers.append(i)

print(numbers)
print('Os números pares são: ')
print(odd_numbers)