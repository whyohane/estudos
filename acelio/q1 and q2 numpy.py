'''1. Crie uma matriz 2 por 2, 3 por 3, 4 por 4, 5 por 5:'''
'''2. Mostre o shape das matrizes criadas.'''
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)

'''3. Crie um array com a função arange() e reformule-a:
In: b = arange(24).reshape(2,3,4)
In: b.shape'''

arr5 = np.arange(24)
print(arr5)

new_arr = arr5.reshape(2,3,4)
print(new_arr)
print(new_arr.shape)

