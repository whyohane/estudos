# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. '''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_plus_5 = []

for x in numbers:
    a = x + 5
    numbers_plus_5.append(a)

print(numbers)
print('Os números da lista adicionados com 5 são:')
print(numbers_plus_5)

