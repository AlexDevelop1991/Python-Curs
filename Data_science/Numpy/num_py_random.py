import numpy as np

print(np.zeros((3, 4)))  # Заполнения массива нулями

print(np.zeros((2, 4), dtype=int))

print(np.ones((5, 4), dtype=int))  # Заполнения массива единицами

ran = np.random.seed(10)  # Начальное число для алгоритма(псевдо случайные числа)
ran = np.random.random((2, 4))  # Генерация случайных чисел
print(ran)

ran2 = np.random.seed(15)
ran2 = np.random.randint(10, 20, size=(2, 4))  # Можно генерировать целые числа
print(ran2)
# Same as random
ran3 = np.random.seed(10)
ran3 = np.random.uniform(size=(3, 5))
print(ran3)

ran4 = np.random.seed(10)
ran4 = np.random.uniform(10.0, 50.0, size=(3, 5))
print(ran4)

ran5 = np.random.seed(10)
ran5 = np.random.choice(np.array([1, 2, 3]), size=10)
print(ran5)

ran6 = np.random.seed(10)
ran6 = np.random.choice(np.array(['a', 'b', 'c']), size=10)
print(ran6)