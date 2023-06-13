'''# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_letter_a = []

for x in fruits:
	
	if "a" in x:
		fruits_with_letter_a.append(x)
        
print(fruits)
print('Frutas que possuem a letra "a" :')
print(fruits_with_letter_a)
		
