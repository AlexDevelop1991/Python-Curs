import pandas as pd
import numpy as np

np.random.seed(1)
n = 100
dates = pd.date_range(start='2050-01-01', periods=n, freq='D')
products = np.random.choice(['Table', 'Camera', 'Phone'], n)
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
df.to_csv('random_sales.csv', index=False)  # Сохоанение Data Frame в CSV файл