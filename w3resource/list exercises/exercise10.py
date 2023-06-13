'''# Exercise 10 - Make a variable named even_numbers that holds only the even numbers '''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
even_numbers = []

for i in numbers:

    if i % 2 == 0:

        even_numbers.append(i)

print(numbers)
print('Os números pares são: ')
print(even_numbers)