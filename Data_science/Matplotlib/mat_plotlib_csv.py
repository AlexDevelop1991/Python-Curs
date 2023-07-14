import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('jersey-rainfall-1984-to-2021.csv', index_col=0)
print(df.head())

df.plot(y='YearTotalmm', kind='area')
plt.show()

df.plot(y='Sep')
plt.show()

df.plot(y=['Apr', 'May'], kind='area')
plt.show()

df.plot()
plt.show()

df.drop(columns=['YearTotalmm']).plot()
plt.show()

print(df.T.head())

df.drop(columns='YearTotalmm').T.plot(y=[1901, 1902], kind='bar')
plt.show()
