import numpy as np

nums_array = np.array([1, 2, 3, 4])  # Создание массива

print(type(nums_array))  # Тип
print(nums_array[0])  # Поиск по индексу в массиве
print(nums_array.shape)  # Показывает форму массива
print(nums_array.ndim)  # Показывает что этот массив является одномернным
print(nums_array.size)  # Количество элементов в этом массиве
print(nums_array.dtype)  # Тип массива
print(nums_array.itemsize)  # Показывает размер каждого элемента в байтах

nums_array2 = np.array([True, 10, 'abc', 5.5])
print(nums_array2.dtype.name)
print(nums_array2.itemsize)

obj_array = np.array([{'city': 'London'}, {'city': 'Boston'}])
print(obj_array.dtype)
print(obj_array.itemsize)

print(np.concatenate((np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]))))  # Соединение одномерных массивов по оси 0