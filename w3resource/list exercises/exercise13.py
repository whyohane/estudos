'''
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
negative_numbers = []

for i in numbers:

    if i < 0:

        negative_numbers.append(i)

print(numbers)
print('Os números negativos são: ')
print(negative_numbers)