'''# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_with_2_or_more_numerals = []

for i in numbers:

    if i > 9 or i < -9:

        numbers_with_2_or_more_numerals.append(i)

print(numbers)
print('Os números que possuem dois algarismos ou mais são: ')
print(numbers_with_2_or_more_numerals)