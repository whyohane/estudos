# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

odd_negative_numbers = []

for x in numbers:

    if x < 0 and x % 2 != 0:
        odd_negative_numbers.append(x)

print(numbers)
print('Os números da lista que são negativos e impares são:')
print(odd_negative_numbers)