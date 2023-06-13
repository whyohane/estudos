'''Exercise 7 - Make a list that contains fruits that have less than 5 characters'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_less_than_5_characters = []

for x in fruits:
    if len(x) < 5:
        fruits_with_less_than_5_characters.append(x)

print(fruits)
print('Frutas que possuem menos de 5 caracteres: ')
print(fruits_with_less_than_5_characters)