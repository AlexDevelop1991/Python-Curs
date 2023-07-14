import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


values = [0, 1, 2, 3, 4, 5, 6, 7]
squares = [value ** 2 for value in values]  # Возводим во вторую степень
print(squares)
plt.plot(values, squares)  # Линейнная диаграмма
# plt.show()

plt.scatter(values, squares)  # Точечная диаграмма
# plt.show()

values = list(range(100))
pows = [pow(value, 3) for value in values]  # Возводим в третью степень
print(pows)
plt.scatter(values, pows)
# plt.show()

plt.scatter(values, pows, c=pows, cmap=plt.cm.Blues, edgecolors='none', s=10)
# plt.show()

values = list(range(50))
squares = [pow(value, 2) for value in values]
cubes = [pow(value, 3) for value in values]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)  # subplots - это подграффики
ax1.scatter(values, squares)    # в данном случаии 2 по вертикали и 1 по горизонтали и sharex значит что ось x общая
ax1.set_title('Square numbers')
ax2.plot(values, cubes)
ax2.set_title('Cube numbers')
# plt.show()

data = {
    'Year': [2001, 2002, 2003, 2004, 2005, 2006],
    'Sales': [100, 150, 130, 180, 230, 270]
}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='line')  # В виде линии
plt.title('Yearly Sales')
# plt.show()

data = {
    'Year': [2001, 2002, 2003, 2004, 2005, 2006],
    'Sales': [100, 150, 130, 180, 230, 270]
}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='bar')  # В виде столбцов
plt.title('Yearly Sales')
# plt.show()

data = {
    'Year': [2001, 2002, 2003, 2004, 2005, 2006],
    'Sales': [100, 150, 130, 180, 230, 270]
}
df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='area')  # В виде линии но что под ней всё закрашенно
plt.title('Yearly Sales')
# plt.show()

data = {
    'Year': [2001, 2002, 2003, 2004, 2005, 2006],
    'Sales': [100, 150, 130, 180, 230, 270]
}
df = pd.DataFrame(data)
df.plot(y='Sales', kind='pie', labels=df['Year'], autopct='%1.1f%%')  # В виде пирога
plt.title('Yearly Sales')
# plt.show()

data = {
    'Age': [25, 28, 32, 41, 42, 42, 50, 59, 60]
}
df = pd.DataFrame(data)
df.plot(y='Age', kind='hist')  # Это гистограмма
plt.title('Age Distribution')
# plt.show()

data = {
    'Category': ['FIRST', 'FIRST', 'SECOND', 'SECOND', 'THIRD', 'THIRD'],
    'Value': [10, 20, 25, 45, 45, 50]
}
df = pd.DataFrame(data)
df.boxplot(by='Category', column='Value')
plt.title('Values Distribution by Category')
# plt.show()

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Week 1 Temp': [6, 10, 12, 14, 17],
    'Week 2 Temp': [8, 12, 13, 14, 18],
    'Week 3 Temp': [9, 11, 14, 16, 20],
    'Week 4 Temp': [10, 15, 10, 17, 22]
}
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)
sns.heatmap(df, cmap='coolwarm', annot=True)
plt.title('Weekly temperature Data')
plt.show()