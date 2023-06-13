'''# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each 
element squared. Output is [4, 9, 16, etc...]'''

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

numbers_squared = []

for x in numbers:
    a = x * x
    numbers_squared.append(a)

print(numbers)
print("As raízes quadradas desses números são:")
print(numbers_squared)