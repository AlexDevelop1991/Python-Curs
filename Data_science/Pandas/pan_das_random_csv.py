import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
n = 100
dates = pd.date_range(start='2050-01-01', periods=n, freq='D')
products = np.random.choice(['Table', 'Camera', 'Phone', 'Microphone', 'Keyboard'], n)
prices = np.round(np.random.uniform(50.0, 200.0, n), 2)
quantities = np.random.randint(1, 15, n)

data = {
    'Date': dates,
    'Product': products,
    'Price': prices,
    'Quantity': quantities
}

df = pd.DataFrame(data)
print(df.head())
print('')
print(df.dtypes)
print('')

df.to_csv('random_sales.csv', index=False)  # Сохранение Data Frame в CSV файл
df = pd.read_csv('random_sales.csv')  # Читает данные из файла CSV в Data Frame
print(df.head())
print(df.dtypes)
print('')

df = pd.read_csv('random_sales.csv', parse_dates=['Date'], date_format='%Y-%m-%d')
print(df.head())
print(df.dtypes)
print('')

df.to_excel('sales_data.xlsx')  # Сохранение Data Frame в Excel файл, прочитать можно так же как и с CVS файлом


df.to_json('sales_data.json')  # Сохранение Data Frame в JSON, прочитать можно так же как и с CVS файлом

print(df.shape)
print('')

print(df.describe().round(2))  # Describe показывает данные только по цифровым колонкам
print('')

product_sales = df.groupby('Product')['Quantity'].sum()  # Просумировали все количества для каждого из товаров
print(product_sales)
print('')

average_prices = df.groupby('Product')['Price'].mean().round(2)  # Нашли среднее значения цены для каждого из товаров
print(average_prices)
print('')

# MATPLOTLIB
plt.bar(product_sales.index, product_sales.values, color=['red', 'blue', 'green', 'pink', 'orange'])  # Создаем диаграмму и задаём индекс и значения
plt.title('Total Sales per Product')  # Задаём названия диаграммы
plt.xlabel('Product', color='yellow')  # Называем ось X
plt.ylabel('Total Sales')  # Называем ось Y
plt.show()  # Чтоб увидить диаграмму


plt.plot(average_prices.index, average_prices.values)
plt.title('Average Price pre Product')
plt.xlabel('Product', color='red')
plt.ylabel('Average Price', color='red')
plt.show()

