import numpy as np

first = np.array([[1, 2, 3], [4, 5, 6]])  # Двухмерный массив
print(first)
print(first.shape)  # Размерность массива то есть 2 ряда и 3 столбца
print(first.ndim)  # Показывает что этот массив двухмерный в данном случаии

second = np.array([[7, 8, 9], [10, 11, 12]])

total = first + second
print(total)

print(first + 1)  # Взяли первый массив и добавили 1 к всем элементам

print(first[1, 1])  # Кординаты на оси в первом массиве цифры 5

print(np.concatenate((first, second)))  # Слияние массивов по оси 0 пр default axis=0

print(np.concatenate((first, second), axis=1))  # Слияние массивов по оси 1

