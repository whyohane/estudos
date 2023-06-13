'''# Exercise 5 - make a list that contains each fruit with more than 5 characters'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_more_than_five_characters = []

for x in fruits:

    if len(x) > 5:
        fruits_with_more_than_five_characters.append(x)

print('Lista de frutas com mais de 5 caracteres: ')
print(fruits_with_more_than_five_characters)