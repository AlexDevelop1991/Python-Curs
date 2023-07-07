import numpy as np

# mas = np.arange(10)
# print(mas)
#
# mas2 = np.arange(15, 25)
# print(mas2)
#
# mas3 = np.arange(start=20, stop=30, step=3)
# print(mas3)
#
# mas4 = np.arange(20).reshape(2, 10)  # Reshape позволяет модифицировать одномерный массив в двухмерный
# print(mas4)
#
# mas5 = np.random.seed(10)
# mas5 = np.random.random((10,))
# print(mas5)
#
# mas6 = np.random.seed(10)
# mas6 = np.random.random((10,)).reshape([2, 5])
# print(mas6)

mas7 = np.random.seed(10)
mas7 = np.random.randint(50, 80, (4, 3, 3))
print(mas7)

mas8 = np.random.seed(10)
mas8 = np.random.randint(50, 80, (4, 3, 3)).flatten()  # Преобразуем в одномерный массив
print(mas8)

