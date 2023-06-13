'''# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_number_characters = []

for x in fruits:
    a = len(x)
    fruits_number_characters.append(a)

print(fruits)
print('O número de caracteres de cada fruta é: ')
print(fruits_number_characters)