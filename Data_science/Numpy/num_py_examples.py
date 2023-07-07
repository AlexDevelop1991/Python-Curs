import numpy as np

# 1.Calculating Total Revenue
prices = np.array([19.99, 29.99, 14.99, 9.99, 24.99])
quantities = np.array([10, 5, 8, 12, 3])

revenue_per_product = prices * quantities
print(revenue_per_product)

total_revenue = np.sum(revenue_per_product)
print(total_revenue)


# 2.Analyzing Blog Post Stats
views = np.array([1000, 500, 800, 1200, 300, 600])

max_views = np.max(views)  # Выводит максимальное значение в массиве
print(max_views)

min_views = np.min(views)  # Выводит минимальное значение в массиве
print(min_views)

mean_views = np.round(np.mean(views), 2)  # Выводит среднее значение в массиве
print(mean_views)

total_views = np.sum(views)  # Суммирует всё в массиве
print(total_views)


# 3.Splitting Order into Batches
order_ids = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008])

batches = np.split(order_ids, 4)  # Разбивает массив на подмассивы
print(batches)

for i, batch in enumerate(batches):  # Делаем итерацию по списку batches, Enumerate возвращает последовать кортежей
    print(f"Batch number {i}:")
    print('First element in the batch: ', batch[0])
    print('Second element in the batch: ', batch[1])
    print('')


# 4.Categorizing Product Ratings
ratings = np.array([4.5, 3.2, 2.8, 5.0, 4.1, 3.9, 2.5, 4.7])

positive_ratings = ratings[ratings >= 4.0]  # Фильтрация массива
print(positive_ratings)

negative_ratings = ratings[ratings < 4.0]
print(negative_ratings)