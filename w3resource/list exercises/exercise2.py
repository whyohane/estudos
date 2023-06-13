'''# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax 
to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

capitalezed_fruits = [x.capitalize() for x in fruits]

print(fruits)
print(capitalezed_fruits)