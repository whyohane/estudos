'''# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
positive_numbers = []

for i in numbers:

    if i >= 0:

        positive_numbers.append(i)

print(numbers)
print('Os números positivos são: ')
print(positive_numbers)