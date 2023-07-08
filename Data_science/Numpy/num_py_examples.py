import numpy as np

                    ### Одномерный массив

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


                    ### Двухмерный массив

# 5.Calculate Total and Average quantities sold
# Each column is specific product (we have 4 products)
# Each row is specific order (we have 2 orders)
order_quantities = np.array([[5, 3, 2, 7], [10, 6, 3, 9]])
print(order_quantities)

# Quantities of the sales per product
total_quantities_sold = np.sum(order_quantities, axis=0)
print(total_quantities_sold)

# Quantities of the sales per order
total_products_pre_order = np.sum(order_quantities, axis=1)
print(total_products_pre_order)

# Average quantities per product across all orders
average_quantities_sold = np.mean(order_quantities, axis=0)
print(average_quantities_sold)


# 6.Calculate Average product Rating and Maximum rating per Category
# Each row is one product
# Each product is rated in 4 categories
product_ratings = np.array([
    [4.5, 3.2, 2.5, 5.0],
    [4.3, 3.8, 1.0, 4.8],
    [2.0, 3.6, 4.7, 0.5]
])

# Average rating in each category
average_rating_per_category = np.mean(product_ratings, axis=0)
print(average_rating_per_category)

# Average rating for each product
average_rating_per_product = np.mean(product_ratings, axis=1)
print(average_rating_per_product)

# Maximum  rating in each category
max_rating_per_category = np.max(product_ratings, axis=0)
print(max_rating_per_category)


                # Трёхмерный массив
# 7.Generation of the sample stock data
companies = ['Google', 'Microsoft', 'Apple']
days = ['Mon 1 April', 'Tue 2 April']
price_types = ['Open', 'Close', 'High', 'Low']

# Shape will be (3, 2, 4)
np.random.seed(1)
stock_prices = np.round(np.random.random((len(companies), len(days), len(price_types))), 3)

for index_axis_0, company in enumerate(companies):
    print(f"Stock prices for the {company}:")
    for index_axis_1, day in enumerate(days):
        print(f"Day: {day}")
        for index_axis_2, price_type in enumerate(price_types):
            print(f"{price_type} Price: {stock_prices[index_axis_0, index_axis_1, index_axis_2]}")
        print('')
    print('')
